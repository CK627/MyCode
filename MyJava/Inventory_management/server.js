const express = require('express');
const mongoose = require('mongoose');
const app = express();


const productRoutes = require('./routes/products');
const adminRoutes = require('./routes/admin');

app.use('/api/products', productRoutes);
app.use('/api/admin', adminRoutes);
app.use(express.json());

const PORT = process.env.PORT || 12345;

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/inventory')
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.log(err));

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
