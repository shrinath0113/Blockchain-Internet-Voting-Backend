from blockchain import blockchain
from ivote import iVoteApp
from flask import jsonify, request
from constants import peers

# endpoint to return the node's copy of the chain.
@iVoteApp.route("/chain", methods=["GET"])
def chain():
    print("/chain Called")
    chain = []
    for block in blockchain.chain:
        chain.append(block.toJson())

    return jsonify(
        {
            "Length": len(chain),
            "Chain": chain,
            "Peers": list(peers),
            "url": request.url,
            "api": "/chain",
        }
    )


def get_chain():
    print("/get_chain Called")
    chain = []
    for block in blockchain.chain:
        chain.append(block.toJson())

    return {
        "Length": len(chain),
        "Chain": chain,
        "Peers": list(peers),
        "url": request.url,
        "api": "/chain",
    }