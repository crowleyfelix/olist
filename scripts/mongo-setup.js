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
            "timestamp": 1456758000.0,
            "call_id": NumberInt(70),
            "source": "99988526423",
            "destination": "9993468278"
        },
        {
            "type": "end",
            "timestamp": 1456765200.0,
            "call_id": NumberInt(70)
        },
        {
            "type": "start",
            "timestamp": 1513098433.0,
            "call_id": NumberInt(71),
            "source": "99988526423",
            "destination": "9993468278"
        },
        {
            "type": "end",
            "timestamp": 1513098896.0,
            "call_id": NumberInt(71)
        },
        {
            "type": "start",
            "timestamp": 1513126076.0,
            "call_id": NumberInt(72),
            "source": "99988526423",
            "destination": "9993468278"
        },
        {
            "type": "end",
            "timestamp": 1513126256.0,
            "call_id": NumberInt(72)
        },
        {
            "type": "start",
            "timestamp": 1513123033.0,
            "call_id": NumberInt(73),
            "source": "99988526423",
            "destination": "9993468278"
        },
        {
            "type": "end",
            "timestamp": 1513123856.0,
            "call_id": NumberInt(73)
        },
        {
            "type": "start",
            "timestamp": 1513061833.0,
            "call_id": NumberInt(74),
            "source": "99988526423",
            "destination": "9993468278"
        },
        {
            "type": "end",
            "timestamp": 1513066256.0,
            "call_id": NumberInt(74)
        },
        {
            "type": "start",
            "timestamp": 1513123033.0,
            "call_id": NumberInt(75),
            "source": "99988526423",
            "destination": "9993468278"
        },
        {
            "type": "end",
            "timestamp": 1513210256.0,
            "call_id": NumberInt(75)
        },
        {
            "type": "start",
            "timestamp": 1513098478.0,
            "call_id": NumberInt(76),
            "source": "99988526423",
            "destination": "9993468278"
        },
        {
            "type": "end",
            "timestamp": 1513098776.0,
            "call_id": NumberInt(76)
        },
        {
            "type": "start",
            "timestamp": 1519865833.0,
            "call_id": NumberInt(77),
            "source": "99988526423",
            "destination": "9993468278"
        },
        {
            "type": "end",
            "timestamp": 1519953056.0,
            "call_id": NumberInt(77)
        }
    ])
});