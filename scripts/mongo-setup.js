conn = new Mongo();

databases = ['olist', 'test']

databases.forEach(database => {
    db = conn.getDB(database);

    //Collections
    db.createCollection('callRecords');
    db.createCollection('phoneBills');


    //Indexes
    db.callRecords.createIndex({ type: 'text', call_id: 1 }, { unique: true })
    db.phoneBills.createIndex({ period: 'text', call_id: 1 }, { unique: true })

    db.callRecords.insertMany([
        {
            "type": "start",
            "timestamp": 1456747200.0,
            "call_id": NumberInt(70),
            "source": "99988526423",
            "destination": "9993468278"
        },
        {
            "type": "end",
            "timestamp": 1456754400.0,
            "call_id": NumberInt(70)
        },
        {
            "type": "start",
            "timestamp": 1513091233.0,
            "call_id": NumberInt(71),
            "source": "99988526423",
            "destination": "9993468278"
        },
        {
            "type": "end",
            "timestamp": 1513091696.0,
            "call_id": NumberInt(71)
        },
        {
            "type": "start",
            "timestamp": 1513118876.0,
            "call_id": NumberInt(72),
            "source": "99988526423",
            "destination": "9993468278"
        },
        {
            "type": "end",
            "timestamp": 1513119056.0,
            "call_id": NumberInt(72)
        },
        {
            "type": "start",
            "timestamp": 1513115833.0,
            "call_id": NumberInt(73),
            "source": "99988526423",
            "destination": "9993468278"
        },
        {
            "type": "end",
            "timestamp": 1513116656.0,
            "call_id": NumberInt(73)
        },
        {
            "type": "start",
            "timestamp": 1513054633.0,
            "call_id": NumberInt(74),
            "source": "99988526423",
            "destination": "9993468278"
        },
        {
            "type": "end",
            "timestamp": 1513059056.0,
            "call_id": NumberInt(74)
        },
        {
            "type": "start",
            "timestamp": 1513115833.0,
            "call_id": NumberInt(75),
            "source": "99988526423",
            "destination": "9993468278"
        },
        {
            "type": "end",
            "timestamp": 1513203056.0,
            "call_id": NumberInt(75)
        },
        {
            "type": "start",
            "timestamp": 1513091278.0,
            "call_id": NumberInt(76),
            "source": "99988526423",
            "destination": "9993468278"
        },
        {
            "type": "end",
            "timestamp": 1513091576.0,
            "call_id": NumberInt(76)
        },
        {
            "type": "start",
            "timestamp": 1519855033.0,
            "call_id": NumberInt(77),
            "source": "99988526423",
            "destination": "9993468278"
        },
        {
            "type": "end",
            "timestamp": 1519942256.0,
            "call_id": NumberInt(77)
        }
    ])
});