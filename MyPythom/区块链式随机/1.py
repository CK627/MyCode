# -*- coding = utf-8 -*-
# @Time:2024/2/19 13:45
# @Author:ck
# @File:1.py
# @Software:PyCharm

import random
import time
from flask import Flask, render_template

app = Flask(__name__)

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.chain.append(block)
        return block

    def get_last_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        proof = random.randint(1, 1000000)
        while not self.valid_proof(previous_proof, proof):
            proof = random.randint(1, 1000000)
        return proof

    def valid_proof(self, previous_proof, proof):
        return (previous_proof * proof) % 23 == 0


# 初始化区块链
blockchain = Blockchain()


@app.route('/')
def index():
    previous_block = blockchain.get_last_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = previous_block['previous_hash']
    block = blockchain.create_block(proof, previous_hash)
    random_number = hash(str(block)) % 53

    return render_template('index.html', random_number=random_number)


if __name__ == '__main__':
    app.run(debug=True)