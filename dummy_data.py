from DB2 import *
from flask import Flask, flash, redirect, render_template, request, session
from sqlalchemy.orm import sessionmaker
rest2 = Resturants(name ="happy hour" , date_posted="2020/01/02",content ="enhance and educate the palate with the freshest ingredients and flavors, while surprising and exciting each guest with personal care and service."  )

db.session.add(rest2)
db.session.commit()

rest3 = Resturants(name ="Root Down" ,date_posted="2020/01/03", content ="Root Down aims to connect the neighborhood to a dining experience in the same way ingredients are connected to food."  )

db.session.add(rest3)
db.session.commit()


rest4 = Resturants(name ="Founding Farmers" ,date_posted="2020/01/04", content ="For us, sustainability is not a lofty idea but a fundamental, and necessary, endeavor. Our concept is about the food and drink of course, but it’s also about our team, our facilities, our practices, and the hundreds of decisions we make each day that affect the world around us."  )

db.session.add(rest4)
db.session.commit()

rest5 = Resturants(name ="Mixt" ,date_posted="2020/01/03", content ="From sprout to plate, we’re all about offering smart, healthy, on-the-go people, smart, healthy, on-the-go food."  )

db.session.add(rest5)
db.session.commit()

rest6 = Resturants(name ="Sweetgreen" ,date_posted="2020/01/03", content ="We believe the choices we make about what we eat, where it comes from and how it’s prepared have a direct and powerful impact on the health of individuals, communities and the environment."  )

db.session.add(rest6)
db.session.commit()

rest7 = Resturants(name ="Panera Bread" ,date_posted="2020/01/03", content ="Food as it should be. Food should taste good. It should feel good. It should do good things for you and the world around you."  )

db.session.add(rest7)
db.session.commit()



print("Finish ")