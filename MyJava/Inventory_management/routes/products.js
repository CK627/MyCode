const express = require('express');
const router = express.Router();
const Product = require('../models/Product');

// Add a new product
router.post('/', async (req, res) => {
    const { name, price, stock } = req.body;
    try {
        const newProduct = new Product({ name, price, stock });
        await newProduct.save();
        res.status(201).json(newProduct);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Get all products
router.get('/', async (req, res) => {
    try {
        const products = await Product.find();
        res.json(products);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

module.exports = router;