from ivote import iVoteApp
from flask import request, jsonify
from blockchain import candidateList, candidates


@iVoteApp.route("/addCandidate", methods=["POST"])
def addCandidate():
    """
    Node-to-Node API\n
    Auhority-to-Node API
    """
    print("/addCandidate Called")
    print("DATA RECIEVED:", request.data)

    try:
        if request.is_json:
            jsonData = request.get_json()

            if (
                "candidateId" in jsonData
                and "candidateName" in jsonData
                and "state" in jsonData
                and "district" in jsonData
                and "ward" in jsonData
            ):
                candidates.addCandidate(
                    jsonData["candidateId"],
                    jsonData["candidateName"],
                    jsonData["state"],
                    jsonData["district"],
                    jsonData["ward"],
                )

                return jsonify(
                    {
                        "result": True,
                        "data": candidateList[-1].toJson(),
                        "api": "/addCandidate",
                        "url": request.url,
                    }
                )
            else:
                return jsonify(
                    {
                        "result": False,
                        "error": "Incomplete Data",
                        "api": "/addCandidate",
                        "url": request.url,
                    }
                )

        else:
            return jsonify(
                {
                    "result": False,
                    "error": "Invalid JSON Format",
                    "api": "/addCandidate",
                    "url": request.url,
                }
            )

    except:
        return jsonify(
            {
                "result": False,
                "error": "Some error occured",
                "api": "/addCandidate",
                "url": request.url,
            }
        )
