conn = new Mongo();

databases = ['olist', 'test']

databases.forEach(database => {
    db = conn.getDB(database);

    //Collections
    db.createCollection('callRecords');
    db.createCollection('phoneBills');

    //Counters
    db.counters.insert({
        '_id': 'call_record_id',
        'sequence_value': NumberInt(-1)
    });

    //Indexes
    db.callRecords.createIndex({ type: 'text', call_id: 1 }, { unique: true })
});