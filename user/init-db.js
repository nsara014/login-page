db = db.getSiblingDB("user_db");
db.user_db.drop();

db.user_db.insertMany([
  {
    id: "001",
    name: "Micheal Reade",
    email: "Mreade@servicenow.com",
    password: "Servicenow0101"
  },
  {
    id: "002",
    name: "Micheal Readee",
    email: "Mreade2@servicenow.com",
    password: "Servicenow0102"
  }
]);
