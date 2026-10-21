from Database_Management import DatabaseManagement
import pandas as pd


class Main:

    def __init__(self):
        self.db = DatabaseManagement()

    def fetch_scanned_barcode(self, product_id, scanned_product_ids, scanned_products_details):

        if product_id not in scanned_product_ids:
            # Add to scanned_product_ids
            scanned_product_ids.append(product_id)

            # Fetch details
            details = self.db.fetch_product_by_id(product_id)
            scanned_products_details.append(list(details))
        else:
            print(f"Product already scanned: {product_id}!!")


if __name__ == "__main__":
    scanned_product_ids = []
    scanned_products_details = []
    main = Main()

    # barcode 1 scanned
    main.fetch_scanned_barcode(1, scanned_product_ids, scanned_products_details)

    # barcode 10 scanned
    main.fetch_scanned_barcode(10, scanned_product_ids, scanned_products_details)

    # barcode 6 scanned
    main.fetch_scanned_barcode(6, scanned_product_ids, scanned_products_details)

    # barcode 1 scanned
    main.fetch_scanned_barcode(1, scanned_product_ids, scanned_products_details)

    # barcode 3 scanned
    main.fetch_scanned_barcode(3, scanned_product_ids, scanned_products_details)

    scanned_products_df = pd.DataFrame(scanned_products_details,
                                       columns=["product_id", "product_name", "quantity", "mrp", "tax", "created_at"])
    scanned_products_df.to_excel("./Products_Scanned.xlsx")
