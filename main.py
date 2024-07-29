import pandas as pd
import self

df = pd.read_csv("Oop exersice/articles.csv", dtype={"id": str})


class Articles:
    def __init__(self, articles_id):
        self.articles_id = articles_id
        self.name = df.loc[df["id"] == self.articles_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.articles_id, "price"].squeeze()

    def available(self):
        in_stock = df.loc[df["id"] == self.articles_id, "in stock"].squeeze()

        return in_stock


class Receipts:
    def __init__(self, article_object):
        self.article = article_object

    def generate(self):
        from fpdf import FPDF

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt no. {self.article.articles_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("Oop exersice/receipt.pdf")


print(df)
articles_id = input("Choose an article to buy: ")
article = Articles(articles_id = articles_id)
if article.available():
    receipt = Receipts(article_object=article)
    receipt.generate()
else:
    print("No Such Article in stock")