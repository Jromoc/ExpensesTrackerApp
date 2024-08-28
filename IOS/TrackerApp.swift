import SwiftUI
import AVFoundation

struct ContentView: View {
    @State private var descripcion: String = ""
    @State private var categoria: String = "Comida"
    @State private var monto: String = ""
    @State private var registros: [Gasto] = UserDefaults.standard.loadGastos() // Cargar los registros guardados
    @State private var showAlert = false

    var body: some View {
        NavigationView {
            VStack {
                Form {
                    TextField("Descripción del gasto", text: $descripcion)
                    
                    Picker("Categoría", selection: $categoria) {
                        ForEach(["Comida", "Transporte", "Entretenimiento", "Ropa", "Otros"], id: \.self) {
                            Text($0)
                        }
                    }
                    
                    TextField("Monto", text: $monto)
                        .keyboardType(.decimalPad)
                    
                    Button(action: agregarGasto) {
                        Text("Agregar Gasto")
                    }
                }
                
                List(registros) { registro in
                    VStack(alignment: .leading) {
                        Text(registro.descripcion)
                            .font(.headline)
                        Text("Categoría: \(registro.categoria)")
                        Text("Monto: \(registro.monto)")
                        Text("Fecha: \(registro.fecha, style: .date)")
                    }
                }
                
                Spacer()
                
                Button(action: iniciarDictado) {
                    Text("Dictar Gasto")
                }
                .padding()
                .alert(isPresented: $showAlert) {
                    Alert(title: Text("Dictado finalizado"), message: Text("El gasto se ha registrado."), dismissButton: .default(Text("OK")))
                }
            }
            .navigationTitle("Registro de Gastos")
            .navigationBarItems(trailing: Button("Borrar Todos") {
                registros.removeAll()
                UserDefaults.standard.saveGastos(registros)
            })
        }
    }
    
    func agregarGasto() {
        guard let montoDouble = Double(monto) else { return }
        
        let nuevoGasto = Gasto(descripcion: descripcion, categoria: categoria, monto: montoDouble, fecha: Date())
        registros.append(nuevoGasto)
        
        // Guardar los registros en UserDefaults
        UserDefaults.standard.saveGastos(registros)
        
        descripcion = ""
        monto = ""
    }
    
    func iniciarDictado() {
        let speechRecognizer = SFSpeechRecognizer(locale: Locale(identifier: "es-MX"))
        let request = SFSpeechAudioBufferRecognitionRequest()
        
        let audioEngine = AVAudioEngine()
        let inputNode = audioEngine.inputNode
        let recognitionTask = speechRecognizer?.recognitionTask(with: request, resultHandler: { result, error in
            if let result = result {
                self.descripcion = result.bestTranscription.formattedString
                self.showAlert = true
                audioEngine.stop()
                inputNode.removeTap(onBus: 0)
            } else if let error = error {
                print("Error: \(error.localizedDescription)")
            }
        })
        
        let recordingFormat = inputNode.outputFormat(forBus: 0)
        inputNode.installTap(onBus: 0, bufferSize: 1024, format: recordingFormat) { (buffer, when) in
            request.append(buffer)
        }
        
        audioEngine.prepare()
        try? audioEngine.start()
    }
}

// Extensiones para UserDefaults para guardar y cargar los registros
extension UserDefaults {
    func saveGastos(_ gastos: [Gasto]) {
        if let encoded = try? JSONEncoder().encode(gastos) {
            set(encoded, forKey: "gastos")
        }
    }
    
    func loadGastos() -> [Gasto] {
        if let savedData = data(forKey: "gastos"),
           let decoded = try? JSONDecoder().decode([Gasto].self, from: savedData) {
            return decoded
        }
        return []
    }
}
