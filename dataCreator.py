#! /usr/bin/python2.7

import json

d = {
 "A": {
            "E": {"best":60,"recent":51,
                    "history": [
					{"date":"5/7", "count": 61},
					{"date":"5/9","count": 59}
                ]
            },
            "D": {"best":60,"recent":51,
                    "history": [
					{"date":"5/7", "count": 61},
					{"date":"5/9","count": 59}
                ]
            },
            "G": {"best":60,"recent":51,
                    "history": [
					{"date":"5/7", "count": 61},
					{"date":"5/9","count": 59}
                ]
            },
          },
 "E": {
            "A": {"best":60,"recent":51,
                    "history": [
					{"date":"5/7", "count": 61},
					{"date":"5/9","count": 59}
                ]
            },
            "D": {"best":60,"recent":51,
                    "history": [
					{"date":"5/7", "count": 61},
					{"date":"5/9","count": 59}
                ]
            },
            "G": {"best":60,"recent":51,
                    "history": [
					{"date":"5/7", "count": 61},
					{"date":"5/9","count": 59}
                ]
            },
          }
}

with open("chordData.json","w") as f:
    json.dumps(str(d),f,indent=1)
