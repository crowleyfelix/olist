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
});