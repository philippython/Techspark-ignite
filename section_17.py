import json

data = {"name":"John", "age":30, "car": None}
data["location"] = "Ogun state"

print(data)
# json - > javascript object notation 
# json is used to send/transfer data across the web

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York", "graduate": false }'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
# print(y)


# a Python object (dict):
data_x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
data_y = json.dumps(data_x)

# the result is a JSON string:
# print(data_y)

big_datax = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(big_datax["cars"][1]["mpg"])
big_datax.get("cars")[1].get("mpg")
# big_datax.get(cars, model, mpg)

print(big_datax["children"][1])
# print(json.dumps(data_x))

complex_dict = {
    "meta": {
        "app": "TechSpark Engine",
        "version": "3.7.1",
        "created_at": "11:12",
        "owner": {
            "name": "Odulaja Philip",
            "id": 35070313,
            "contacts": {
                "email": "philip@example.com",
                "phones": ["+2347012345678", "+2348098765432"]
            }
        }
    },

    "tenants": {
        "default": {
            "id": "tn-000",
            "features": ["analytics", "realtime-stream", "access-control"],
            "limits": {"projects": 10, "storage_gb": 50}
        },
        "partners": [
            {
                "id": "tn-101",
                "name": "Alpha Labs",
                "roles": {
                    "admins": [{"uid": "u1", "since": "2023-06-12"}],
                    "developers": [{"uid": "u2", "languages": ["python", "js"]}]
                },
                "integration": {
                    "oauth": {"client_id": "abc", "scopes": ["read", "write"]},
                    "webhooks": [
                        {"url": "https://alpha.example/hook", "active": True, "retries": 3}
                    ]
                }
            },
            {
                "id": "tn-102",
                "name": "Beta Corp",
                "roles": {"admins": [], "developers": []},
                "notes": None
            }
        ]
    },

    "dataset": {
        "schema": {
            "fields": [
                {"name": "timestamp", "type": "datetime", "nullable": False},
                {"name": "sensor_id", "type": "string", "nullable": False},
                {"name": "values", "type": "array", "items": "float", "nullable": True}
            ],
            "primary_key": ["timestamp", "sensor_id"]
        },
        "samples": [
            {"timestamp": "2024-06-01T12:00:00Z", "sensor_id": "S01", "values": [0.12, 0.15]},
            {"timestamp": "2024-06-01T12:01:00Z", "sensor_id": "S01", "values": [0.11, 0.14]},
        ],
        # nested numeric-matrix example
        "calibration": {
            "matrix": [[1.0, 0.0, -0.01], [0.0, 0.98, 0.02], [0.0, 0.0, 1.0]],
            "versioned": {"v1": {"applied_by": "engine"}, "v2": {"applied_by": "admin"}}
        }
    },

    "access_control": {
        "policies": [
            {
                "policy_id": "p-read-1",
                "effect": "allow",
                "actions": ["read", "list"],
                "resource": "dataset.samples",
                "conditions": {"ip": ["196.0.0.0/8"], "time": {"start": "08:00", "end": "18:00"}}
            },
            {
                "policy_id": "p-admin",
                "effect": "allow",
                "actions": ["*"],
                "resource": "*",
                "meta": {"created_by": "system"}
            }
        ],
        # mapping users to policies
        "assignments": {
            "u1": ["p-admin"],
            "u2": ["p-read-1"]
        }
    },

    "jobs": {
        "queue": [
            {"job_id": "j-001", "type": "train", "params": {"epochs": 10, "lr": 0.001}, "owner": "u2"},
            {"job_id": "j-002", "type": "eval", "params": {"batch": 64}, "owner": "u3"},
        ],
        "history": {
            "j-000": {"status": "completed", "duration_s": 534.2, "metrics": {"acc": 0.913}},
        }
    },

    "metrics": {
        "recent": [{"name": "cpu", "value": 0.24}, {"name": "mem", "value": 0.512}],
        "aggregates": {"daily": {"max_cpu": 0.98, "avg_mem": 0.42}}
    },

    "binary": {
        # bytes stored as hex string for JSON-safe transport
        "model_blob_hex": "4f6b2a9b..."
    },

    "notes": [
        ("todo", {"task": "add export", "priority": "high"}),
        ("done", {"task": "init pipeline", "completed_at": "2024-06-01T13:00:00Z"})
    ],

    # example of metadata linking to external resources
    "external": {
        "git": {"repo": "https://github.com/techspark/engine", "branch": "main"},
        "docs": [{"title": "Design", "link": "https://docs.example/design"}]
    }
}

print(complex_dict["meta"]["owner"]["contacts"]["phones"][0])

with open("practice.json", "x") as json_file:
    json.dump(complex_dict, json_file, indent=4, sort_keys=True)

# dumps is used when you want to convert dictionary to json and dump -> used when you want dump the json into a file