import pandas as pd
import numpy as np
from sklearn.base import TransformerMixin


class BreadBasketCleaner(TransformerMixin):
    def __init__(self, withItems=False, withDays=False):
        self.withItems = withItems
        self.withDays = withDays

    def fit(self, breadbasket):
        breadbasket['DateTime'] = pd.to_datetime(
            breadbasket.Date + ' ' + breadbasket.Time)
        groups = {
            "beverage": ['Hot chocolate', 'Coffee', 'Tea', 'Mineral water', 'Juice', 'Coke', 'Smoothies'],
            "kids": ["Ella's Kitchen Pouches", 'My-5 Fruit Shoot', 'Kids biscuit'],
            "snacks": ['Mighty Protein', 'Pick and Mix Bowls', 'Caramel bites', 'Bare Popcorn', 'Crisps', 'Cherry me Dried fruit', 'Raw bars'],
            "bread": ['Bread', 'Toast', 'Baguette', 'Focaccia', 'Scandinavian'],
            "breakfast_pastry": ['Muffin', 'Pastry', 'Medialuna', 'Scone'],
            "dessert": ['Cookies', 'Tartine', 'Fudge', 'Victorian Sponge', 'Cake', 'Alfajores', 'Brownie', 'Bread Pudding', 'Bakewell', 'Raspberry shortbread sandwich', 'Lemon and coconut', 'Crepes', 'Chocolates', 'Truffles', 'Panatone'],
            "condiments": ['Jam', 'Dulce de Leche', 'Honey', 'Gingerbread syrup', 'Extra Salami or Feta', 'Bacon', 'Spread', 'Chimichurri Oil'],
            "breakfast": ['Eggs', 'Frittata', 'Granola', 'Muesli', 'Duck egg', 'Brioche and salami'],
            "lunch": ['Soup', 'Sandwich', 'Chicken sand', 'Salad', 'Chicken Stew']
        }

        def chooseCat(prod):
            for groupName, groupItems in groups.items():
                if prod in groupItems:
                    return groupName
            return "OTHER_FOOD"

        breadbasket["category"] = breadbasket.Item.apply(chooseCat)
        breadbasket = pd.get_dummies(
            breadbasket, columns=["category"], prefix="", prefix_sep="")
        breadbasket = breadbasket.drop(columns=["Date", "Time"])
        if self.withItems:

            bread_group1 = breadbasket.groupby(['Transaction', 'DateTime']).agg({
                'Item': lambda x: list(x)})
            bread_group2 = breadbasket.groupby(
                ['Transaction', 'DateTime']).sum()
            bread_group = pd.concat([bread_group1, bread_group2], axis=1)

            bread_group.reset_index(level=['DateTime'], inplace=True)
        else:
            bread_group = breadbasket.groupby(
                ['Transaction', 'DateTime']).sum()
            bread_group.reset_index(level=['DateTime'], inplace=True)

        bread_group['hour'] = bread_group.DateTime.dt.hour
        if self.withDays:
            bread_group['day'] = bread_group.DateTime.dt.day_name()
        else:
            bread_group['day'] = bread_group.DateTime.dt.dayofweek

        bread_group.drop(columns=["DateTime"], inplace=True)

        self.bread_group = bread_group
        return self

    def transform(self, x):
        return self.bread_group
