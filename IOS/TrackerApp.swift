import SwiftUI

struct ContentView: View {
    @State private var descripcion: String = ""
    @State private var categoria: String = "Comida"
    @State private var monto: String = ""
    @State private var registros: [Gasto] = []
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
            }
            .navigationTitle("Registro de Gastos")
        }
    }
    
    func agregarGasto() {
        guard let montoDouble = Double(monto) else { return }
        
        let nuevoGasto = Gasto(descripcion: descripcion, categoria: categoria, monto: montoDouble, fecha: Date())
        registros.append(nuevoGasto)
        
        descripcion = ""
        monto = ""
    }
}

struct Gasto: Identifiable {
    var id = UUID()
    var descripcion: String
    var categoria: String
    var monto: Double
    var fecha: Date
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
