import streamlit as st

st.write('Hello, I am Sumit, Welcome to my quiz Zone.. Hope you like the game. You may please Proceed further for gaming...')
("welcome to the quiz game .....\n")	

st.write('1.Which river is widely recognized as the longest river in the world    \nA.Amazon River  \nB.Nile River  \nC.Yangtze River  \nD.Mississippissouri River System')
ans1 = st.text_input('enter your choice 1....')
st.write('2.The Code of Hammurabi, one of the oldest deciphered writings of significant length in the world, originated from which ancient civilization?\nA.Ancient Egypt\nB.Indus Valley Civilization\nC.Babylonian Empire\nD.Ancient Greece')
ans2 = st.text_input('enter your choice 2....')
st.write('3.Which of the following is the smallest individual bone in the human body?\nA.Stapes\nB.Malleus\nC.Incus\nD.Patella')
ans3 =  st.text_input('enter your choice 3....')
st.write('who is the national animal of india?\nA.bear\nB.giraffe\nC.lion\nD.tiger')
ans4 =  st.text_input('enter your choice 4....')
st.write('5.A system of government in which power is constitutionally divided between a central national government and individual regional or state governments is called: \nA.Unitary system\nB.Federal system\nC.Oligarchy  \nD.Confederacy')
ans5 =  st.text_input('enter your choice 5....')
st.write('6.The Andes mountain range, the longest continental mountain range in the world, runs along the western edge of which continent\nA.NorthAmerica \nB.Asia\nC.South America\nD.Africa')
ans6 =  st.text_input('enter your choice 6....')
st.write('7.The fall of the Berlin Wall, which symbolized the collapse of the Iron Curtain and paved the way for German reunification, occurred in what year?  \nA.1989\nB.1991\nC.1975\nD.1981')
ans7 =  st.text_input('enter your choice 7....')
st.write('8.Which specific chamber of the human heart is responsible for pumping oxygen-rich blood directly into the aorta and out to the rest of the body?  \nA.Right atrium\nB.Left atrium\nC.Right ventricle\nD.Left ventricle')
ans8 =  st.text_input('enter your choice 8....')
st.write('9.Which subatomic particle carries a negative electric charge and orbits the nucleus of an atom? \nA.Proton\nB.Electron\nC.Neutron\nD.Positron')
ans9 =  st.text_input('enter your choice 9....')
st.write('10.In which European city is the headquarters of the International Court of Justice (ICJ) located? \nA.Geneva\nB.Brussels\nC.The Hague\nD.Vienna')
ans10 =  st.text_input('enter your choice10....')
total = 0
if ans1 == 'b' or ans1 == 'B':
 total+= 4
if ans2 == 'c' or ans2 == 'C':
 total+= 4
if ans3 == 'a' or ans3 == 'A':
 total+= 4
if ans4 == 'd' or ans4 == 'D':
 total+= 4
if ans5 == 'b' or ans5 == 'B':
 total+= 4
if ans6 == 'c' or ans6 == 'C':
 total+= 4
if ans7 == 'a' or ans7 == 'A':
 total+= 4
if ans8 == 'd' or ans8 == 'D':
 total+= 4
if ans9 == 'b' or ans9 == 'B':
 total+= 4
if ans10 == 'c' or ans10 == 'C':
 total+= 4

st.write(total) 

if total == 40: 
   st.write('congratulation..you have 1st position')
if total == 30:
   st.write('congratulation you have 2nd position')
if total == 20:
   st.write('congratulation you have passed the quiz')
else:
   st.write('better luck next time')  
