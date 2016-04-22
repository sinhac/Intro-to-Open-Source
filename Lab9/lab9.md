db.definitions.find(): prints all the lines with the word "definition"
db.definitions.findOne(): prints only one line with the word "definition"
db.definitions.find({word: "Capitaland"}): prints the lines that match the pattern described in the curly braces
db.definitions.find({_id: ObjectId("56fe9e22bad6b23cde07b8ce")}) outputs { "_id" : ObjectId("56fe9e22bad6b23cde07b8ce"), "definition" : " n.  (RPI) The ubiquitous supermarket of the Capital District and all-time favorite food store for RPI students.  Also called ``Price Gouger'' or ``Price Hacker.''", "word" : "Chopper" }


Word that I'm adding: db.definitions.insert({word: "bumfuzzle", definition: "to confuse, befuddle"})
My update: db.definitions.update({_id: ObjectId("57072ad608bac2725f1143b1")}, {"definition":" v. to confuse, befuddle","word":"Bumfuzzle"})
