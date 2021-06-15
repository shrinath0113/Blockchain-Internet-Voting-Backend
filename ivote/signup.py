from database.model import Voter
from ivote import iVoteApp, voterDb
from flask import request, jsonify
from werkzeug.security import generate_password_hash


@iVoteApp.route("/signup", methods=["POST"])
def signup():
    """
    Client-to-Authority API
    """

    print("/signup Called")
    print("DATA RECIEVED:", request.data)

    try:
        if request.is_json:
            jsonData = request.get_json()

            if (
                "voterId" in jsonData
                and "name" in jsonData
                and "state" in jsonData
                and "district" in jsonData
                and "ward" in jsonData
                and "mobile" in jsonData
                and "password" in jsonData
            ):
                voter = Voter(
                    voterId=jsonData["voterId"],
                    name=jsonData["name"],
                    state=jsonData["state"],
                    district=jsonData["district"],
                    ward=jsonData["ward"],
                    mobile=jsonData["mobile"],
                    passwordHash=generate_password_hash(jsonData["password"]),
                )
                print("adding data")
                # insert user
                # voterDb.session.add(voter)
                # voterDb.session.commit()
                added = voterDb.addVoter(voter)
                if added:
                    print("adding done")
                    return (
                        jsonify(
                            {
                                "result": True,
                                "api": "/signup",
                                "result": "Successful Registration",
                                "url": request.url,
                            }
                        ),
                        200,
                    )
                else:
                    print("Could not Add User")
                    return jsonify(
                        {
                            "result": False,
                            "api": "/signup",
                            "error": "Registration Failed in Database",
                            "url": request.url,
                        }
                    )

            else:
                return jsonify(
                    {
                        "result": False,
                        "error": "Incomplete Data",
                        "api": "/signup",
                        "url": request.url,
                    }
                )

        else:
            return jsonify(
                {
                    "result": False,
                    "error": "Invalid JSON Format",
                    "api": "/signup",
                    "url": request.url,
                }
            )

    # except IntegrityError:
    #     voterDb.session.rollback()
    #     return jsonify(
    #         {
    #             "result": False,
    #             "error": "Voter Db Rollback\nUser already exists",
    #             "api": "/signup",
    #             "url": request.url,
    #         }
    #     )
    # except AttributeError:
    #     return jsonify(
    #         {
    #             "result": False,
    #             "error": "Provide data in json format",
    #             "api": "/signup",
    #             "url": request.url,
    #         }
    #     )

    except:
        return jsonify(
            {
                "result": False,
                "error": "Some error occured",
                "api": "/signup",
                "url": request.url,
            }
        )
