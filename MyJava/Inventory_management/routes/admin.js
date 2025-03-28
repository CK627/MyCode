const express = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const router = express.Router();
const Admin = require('../models/Admin');

// Register a new admin
router.post('/register', async (req, res) => {
    const { username, password } = req.body;
    try {
        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(password, salt);

        const newAdmin = new Admin({ username, password: hashedPassword });
        await newAdmin.save();
        res.status(201).json(newAdmin);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Login admin
router.post('/login', async (req, res) => {
    const { username, password } = req.body;
    try {
        const admin = await Admin.findOne({ username });
        if (!admin) return res.status(400).json({ msg: 'User does not exist' });

        const isMatch = await bcrypt.compare(password, admin.password);
        if (!isMatch) return res.status(400).json({ msg: 'Invalid credentials' });

        const token = jwt.sign({ id: admin._id }, 'jwtSecret', { expiresIn: 3600 });
        res.json({ token, admin: { id: admin._id, username: admin.username } });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

module.exports = router;