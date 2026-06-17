# 📊 Data Folder

This folder contains the data files used by the Birthday Email Sender application.

## 📄 Files

### `Birthday_Wish_Template.txt`
The email template containing the birthday message body. Features:
- Placeholder `{name}` - replaced with recipient's name
- Placeholder `[Your Name]` - replaced with sender's name
- Heartfelt birthday wishes and encouragement
- Professional tone with warm closing

**Usage**: Read by `app.py` and personalized before being converted to HTML.

### `products.csv`
Sample product inventory data with the following columns:
- **product_id**: Unique identifier
- **product_name**: Name of the product
- **category**: Product category (Electronics, Furniture, Kitchen, Sports, etc.)
- **brand**: Brand name
- **sku**: Stock Keeping Unit
- **price_usd**: Price in USD
- **cost_usd**: Cost in USD
- **profit_margin_%**: Profit margin percentage
- **stock_quantity**: Quantity in stock
- **unit**: Unit of measurement
- **weight_kg**: Weight in kilograms
- **dimensions_cm**: Product dimensions
- **color**: Product color
- **material**: Material composition
- **rating**: Customer rating (out of 5)
- **reviews_count**: Number of reviews
- **supplier**: Supplier name
- **country_of_origin**: Country of manufacture
- **warranty_years**: Warranty duration
- **is_active**: Whether product is currently active

**Note**: This file is for reference/sample data. It's not currently used in the email sending functionality but can be integrated for sending product-related promotions on birthdays.

## 🔧 How to Customize

### Modify the Birthday Template
Edit `Birthday_Wish_Template.txt`:
1. Keep `{name}` placeholder for recipient name
2. Keep `[Your Name]` placeholder for sender name
3. Write your personalized message
4. Use blank lines to separate paragraphs

### Add Product Data
To incorporate product recommendations into birthday emails:
1. Read `products.csv` using pandas
2. Select relevant products
3. Insert product info into the email template

Example code:
```python
import pandas as pd

df = pd.read_csv('data/products.csv')
# Filter products and include in email
```

## 💡 Future Enhancements

- [ ] Create product recommendation logic for birthday emails
- [ ] Add multiple email templates for different occasions
- [ ] Generate templates from CSV
- [ ] Support CSV-based recipient lists
