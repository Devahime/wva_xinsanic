from database.database import get_db

class RestauraceService:
    @staticmethod
    def get_all(kategorie_id = None):
        db = get_db()

        sql = "SELECT DISTINCT * FROM restaurace JOIN restaurace_kategorie USING(restaurace_id) WHERE 1=1"
        arguments = []
        if kategorie_id is not None:
            sql += " AND kategorie_id = ?"
            arguments.append(kategorie_id)
        else:
            sql = "SELECT DISTINCT nazev, restaurace_id, obrazekrestaurace FROM restaurace JOIN restaurace_kategorie USING(restaurace_id) WHERE 1=1"
        return db.execute(sql, arguments).fetchall()

    @staticmethod
    def get_by_category(kategorie_id: int):
        db = get_db()
        return db.execute(
            "SELECT * FROM restaurace JOIN restaurace_kategorie USING(restaurace_id) WHERE restaurace_kategorie.kategorie_id= ?",
            [kategorie_id]
        ).fetchall()

    @staticmethod
    def get_category_name(kategorie_id: int):
        db = get_db()
        return db.execute(
            "SELECT * FROM kategorie WHERE kategorie_id = ?",
            [kategorie_id]
        ).fetchone()

    @staticmethod
    def get_by_id(restaurace_id: int):
        db = get_db()
        return db.execute(
            "SELECT * FROM restaurace WHERE restaurace_id = ?",
            [restaurace_id]
        ).fetchone()

    @staticmethod
    def najit_restauraci(user_id):
        db = get_db()
        sql = "SELECT * FROM restaurace WHERE uzivatel_id = ?"
        return db.execute(sql, (user_id,)).fetchone()[0]

