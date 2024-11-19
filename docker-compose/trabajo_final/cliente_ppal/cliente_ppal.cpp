#include <iostream>
#include <pqxx/pqxx>

int main() {
    try {
        pqxx::connection c("dbname=db_ppal user=postgres_ppal password=postgres_ppal host=pg_ppal port=5432");
        if (c.is_open()) {
            std::cout << "Conectado a la base de datos: " << c.dbname() << std::endl;
        } else {
            std::cout << "No se pudo conectar a la base de datos" << std::endl;
            return 1;
        }

        pqxx::nontransaction w(c);
        pqxx::result r = w.exec("SELECT * FROM tabla_x");

        std::cout << "ID\tNombre\tValor" << std::endl;
        for (auto row : r) {
            std::cout << row["id"].as<int>() << "\t"
                      << row["nombre"].c_str() << "\t"
                      << row["valor"].as<int>() << std::endl;
        }

        c.disconnect();
    } catch (const std::exception &e) {
        std::cerr << e.what() << std::endl;
        return 1;
    }

    return 0;
}
