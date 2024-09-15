db = db.getSiblingDB("user_db");
db.user_db.drop();

db.user_db.insertMany([
  {
    id: "001",
    name: "Micheal Reade",
    email: "samplename@sample.com",
    password: "Password1"
  },
  {
    id: "002",
    name: "Micheal Readee",
    email: "Samplename2@sample.com",
    password: "Password2"
  }
]);
