from nltk.chat.util import Chat, reflections
import pyttsx3
import speech_recognition as sr
import wolframalpha 
app_id = "HPEGVV-T8WLEEJ734" 
client = wolframalpha.Client(app_id)
r = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names()
# initialisation
engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 10.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# testing
##engine.say("My first code on text-to-speech")


pairs = [
    [
        r"GLA University(.*)",
        [
            "G L A University is one of the best private universities in Uttar Pradesh \nIt is ranked top most among the private colleges"]
    ],

    [
        r"(.*)courses offered by GLA(.*)",
        ["G L A University,Mathura, Uttar Pradesh has 83 Courses with Average Fees 1,57500 per year"]
    ],

    [
        r"(.*)founder of GLA(.*)",
        ["G L A University is established by the current Chancellor, Shri Narayan Das Agrawal in 1998 "]
    ],

    [
        r"(.*)deparments in GLA(.*)",
        [
            "Computer Engineering & Applications Electrical Engineering Electronics & Communications Mechanical Engineering Civil Engineering"]
    ],

    [
        r"(.*)project mentor(.*)",
        ["Mr. Amir khan is our project mentor. He is faculty of Training and Development Department"]
    ],

    [
        r"(.*)total number of students(.*)",
        ["The university is home to more than 12,000 students enrolled in a variety of professional courses"]
    ],

    [
        r"(.*)number of companies visiting(.*)",
        ["150+ companies visited GLA University in the session 2019-2020. This also contains many MNC's."]
    ],

    [
        r"(.*)highest package(.*)",
        ["22 lakhs per annum is the  Highest Package Offfered"]
    ],

    [
        r"(.*)facilities provided to students(.*)",
        [
            "A Well designed and maintained buildings, contemporary laboratories, spacious residential complexes and recreational fascilities makes the campus one of the best in the regions and gives its students an edge over their counterparts coming from other universities"]
    ],

    [
        r"(.*)facilities provided to hostel inmates(.*)",
        [
            "GLA Hostels offers many facilities such as gym, Common room, Canteen, Departmental store, Ground, internet facility, 24 x 7 Water and electricity,Stationary, Library, auditorium, Dispensary"]
    ],

    [
        r"(.*)cse department(.*)",
        [
            "Department of Computer Engineering and Applications at GLA University offers various programs at both under graduate and post graduate level. All the programs feature a combination of theoretical and practical elements in order to provide the students a platform to correlate the learning. In addition, guest lectures and talks by eminent persons from industry and academia are frequently arranged to keep the students abreast with the latest technologies"]
    ],

    [
        r"(.*)electrical Department(.*)",
        [
            "Electrical Engineering is one of the fastest growing fields that involves the study and application of electricity and electronics. It is the most interesting branch of engineering because it involves the study of computer, electrical and electronics and communication. Electrical engineering deals with generation, transmission and distribution of electricity"]
    ],

    [
        r"(.*)mechanical Department(.*)",
        [
            "The department of Mechanical Engineering blossoms with the specialized technical and professional excellence.The department is constantly decisive to educate the mechanical engineers of tomorrow by integrating the theoretical and practical knowledge and accentuating on the learning and critical thinking."]
    ],

    [
        r"(.*)civil Department(.*)",
        [
            "Civil Engineering is concerned with the improvement in quality of basic needs of human civilization and taking care of the naturally and humanly built environments with their planning, designing, construction, operation and maintenance. "]
    ],

    [
        r"(.*)electronics and communication department(.*)",
        [
            "Department aims to provide quality education in the domain of Electronics and Communication Engineering through periodically updated curriculum, effective teaching learning process, state of the art laboratory facilities and collaborative ventures with the industries."]
    ],

    [
        r"(.*)pro VC(.*)",
        ["Mr. Professor D. S. Chauhan"]
    ],

    [
        r"(.*)hod of CSE Department(.*)",
        ["Dr. Anand Singh Jalal H.O. D. & Professor, Department of Computer Engineering & Applications"]
    ],

    [
        r"(.*)director(.*)",
        [
            "Dr. Anoop Kumar Gupta is currently positioned as the Director at G L A University, Mathura. Dr. Gupta has implemented the e-Governance project at GLA University as well as overseen the website and brochure of the University."]
    ],

    [
        r"(.*)cafeteria Facility(.*)",
        [
            "We have 4 cafeterias in campus that helps the students to fulfil their cravings as and when they want. The cafeteria offers a good menu of multi-cuisine delights, amidst a lively, jolly atmosphere."]
    ],

    [
        r"(.*)medical facility(.*)",
        ["24*7 hours medical facility is available in our university"]
    ],

    [
        r"(.*)address(.*)",
        ["17km Stone, NH-2, Mathura-Delhi Road Mathura, Chaumuhan, Uttar Pradesh 281406"]
    ],

    [
        r"(.*)code of conduct and Ethics policy(.*)",
        [
            "For information about code of conduct and ethics policy, please visit:http://www.gla.ac.in/Uploads/image/98imguf_GLA-University--Code-of-Conduct-and-Ethics-Policy-Updated.pdf"]
    ],

    [
        r"(.*)chancellor Information(.*)",
        ["Mr.Narayan Das Agrawal."]
    ],

    [
        r"(.*)deans Info(.*)",
        [
            "Prof. (Dr.) Anup Kumar Gupta(Dean Academic Affairs),Prof. (Dr.) Anirudha Pradhan(Professor of Mathematics & Dean Research & Development),Prof. (Dr.) D.K. Das(Dean of Student's Affairs)."]
    ],

    [
        r"(.*)registrar Info(.*)",
        ["Mr. Ashok Kumar Singh."]
    ],

    [
        r"(.*)training and placement department(.*)",
        [
            " G L A University has training and placement department i.e Placement training plays a major role in shaping up the career goals of students. It is the dream of every engineering student to get placed in a top organization visiting their campus for recruitment.Training of students and equipping them with life skills has become an important responsibility of the institution."]
    ],

    [
        r"(.*)training and development department(.*)",
        [
            "G L A University has training and development department i.e. Training and development refers to educational activities within a company created to enhance the knowledge and skills of employees while providing information and instruction on how to better perform specific tasks."]
    ],

    [
        r"(.*)executive Council(.*)",
        [
            "Mr. Narayan Das Agrawal (Business)Chairperson and many more.for further details visit : https://www.gla.ac.in/about-us/executive-council."]
    ],

    [
        r"(.*)library information(.*)",
        ["There are more than 155000 books available in our library."]
    ],

    [
        r"(.*)library Timigs(.*)",
        ["Library timings is from 8 am to 11 pm for boys and for girls it is form 8 am to 6 pm."]
    ],

    [
        r"(.*)library facilities(.*)",
        [
            "the Central Library has more than 169899 books over 4,500 CD-ROMs and subscribes to more than 95 national and international journals/magazines in print besides a larger number of e-journals through INDEST-AICTE Consortium for Subscription of International Journals of IEEE/IEE (IEL Online+ASPP), ASME are available to the academic community all over the campus. "]
    ],

    [
        r"(.*)courses offered(.*)",
        [
            "BA LLB, BBA LLB, BA [Hons.], BBA, BBA [Hons.], B.Com [Hons.], BCA, B.Ed, B.Pharm, B.Sc [Hons.], B.Tech, MA, MBA, MCA, M.Pharm, M.Sc, M.Tech, Diploma, Post Graduate Diploma, Advanced Diploma, Certificate, Ph.D."]
    ],

    [
        r"(.*)founder of GLA University(.*)",
        ["Shri Narayan Das Agrawal is the founder of g l a university and was established in 1998"]
    ],

    [
        r"(.*)aim of GLA(.*)",
        [
            "The aim of G L A is to provide education of high quality to fulfill the needs of higher education in the society."]
    ],

    [
        r"(.*)recent events held(.*)",
        ["Milan 2019 ,sky light, cultural night, battle of dance etc."]
    ],

    [
        r"(.*)fees of different courses(.*)",
        ["B.Tech(CSE):1,60,000;B.Tech(ECE):1,40,000;B.Tech(ME):1,40,000"]
    ],

    [
        r"(.*)total number of students(.*)",
        ["More than 12000 students."]
    ],

    [
        r"(.*)nuumber of faculty in GLA university(.*)",
        ["There are over 600 faculty in G L A."]
    ],

    [
        r"(.*)contact details and Contact number(.*)",
        ["For any query, you can call : 8937099911, 6399020003,6399020004, 6399020005."]
    ],

    [
        r"(.*)admission help/ helpline(.*)",
        ["For admission related information, you can call : 6399020004, 6399020005"]
    ],

    [
        r"(.*)recruiters(.*)",
        [
            "Our recruiters are Tata, HCL, capgemini, accenture, amazon, honda, infosys, wipro, samsung, microsoft, honda, oppo, alight, VVDN,  any many more."]
    ],

    [
        r"(.*)fee structure MSc. , PhD. , BBA(.*)",
        [
            "BBA ranges from INR 82,000 to INR 86,000 per annum,M.Sc ranges from INR 50,000 to INR 118,000 per annum,Ph.D course varies from INR 73,000 to INR 79,000 per annum."]
    ],

    [
        r"(.*)scholarship details/ discount details(.*)",
        ["Scholarship of 33000 is given to those students who have secured more than 90% marks in PCM in Intermediate."]
    ],

    [
        r"(.*)top 5 recruiters at GLA(.*)",
        ["Our top recruiters are:Amazon, microsoft, accenture, salesforce, samsung."]
    ],

    [
        r"(.*)IQAC(.*)",
        [
            "The Internal Quality Assurance Cell (IQAC) was constituted in GLA University on January 4, 2016,with the aim of working towards realization of the goals of quality enhancement and sustenance through internalization of quality culture and institutionalization of best practices."]
    ],

    [
        r"(.*)NIRF(.*)",
        [
            "The methodology draws from the overall recommendations broad understanding arrived at by a Core Committee set up by MHRD, to identify the broad parameters for ranking various universities and institutions."]
    ],

    [
        r"(.*)alumni of our university(.*)",
        ["More than 2000+ G L Aians are Working Abroad with the most reputed companies."]
    ],

    [
        r"(.*)workshops held(.*)",
        [
            "There are various workshops that takes place in the Univeristy from each department,These are related to almost every course of our college that helps students to expnand their knowledge."]
    ],

    [
        r"(.*)awards and achievements(.*)",
        [
            "G L A University is on 2nd rank in Uttar Pradesh and on 6th rank in all over India,It is rated 'AAA' among India's best engineering colleges."]
    ],

    [
        r"(.*)number of hostlers(.*)",
        [
            "We have 15 boys hostels and 4 girls hostels that have about 5000+ residents,our college has 4500+ boys and 1500+ girls hostlers."]
    ],

    [
        r"(.*)hostel fees details of AC or Non AC(.*)",
        [
            "For boys, AC hostel rooms are available at 65000 whereas non AC wings are available at 50000,For girls, single seater room is available at 41000 whereas for double seater it is 43000."]
    ],

    [
        r"(.*)hostel details(.*)",
        ["There are facilities for indoor and outdoor games. Green lawns are provided,24x7 electric and power supply."]
    ],

    [
        r"(.*)new Generation IEDC(.*)",
        [
            "New Generation Innovation and Entrepreneurship Development Centre(NewGen IEDC) is a programme launched by National Science and Technology Entrepreneurship Development Board (NSTEDB), Department of Science & Technology (DST), Government of India."]
    ],

    [
        r"(.*)no Ragging policy(.*)",
        ["Ragging is strictly prohibited in our campus."]
    ],

    [
        r"(.*)hostel security(.*)",
        [
            "hostels are provided 24 hours security with our best group of guards. Students are 24 hours under surveillance and biometric is compulsory for every student."]
    ],

    [
        r"(.*)about GLAMS portal(.*)",
        ["for the ease of students to access their information, we have provided an online portal."]
    ],

    [
        r"(.*)attendence criteria(.*)",
        ["It is mandatory to fullfil 75% attendance for each student"]
    ],

    [
        r"(.*)leave and Outing details(.*)",
        [
            "girls are provided outing till 6.30 pm whereas boys till 8pm and it is compulsory for everyone to follow the timing criteria of leave and outing"]
    ],

    [
        r"(.*)institutes(.*)",
        [
            "The institutes under the university are as follows: Institute of Engineering and Technology, Institute of Applied Science and Humanities, Institute of Business Management"]
    ],

    [
        r"(.*)why GLA University(.*)",
        [
            "At G L A University we offer a nurturing environment that fosters sharp learning skills, a top-of-the-line curriculum that offers the best in education along with pioneering placement opportunities."]
    ],

    [
        r"(.*)sports Facilities(.*)",
        [
            "All the playing grounds are located strategically across the university thereby making sports part of one's life no matter where the person is in the university. G L A IPL (G L A Cricket Championship), Volleyball, Football, Badminton, Basketball, Chess tournaments every year."]
    ],

    [
        r"(.*)campus Facilities(.*)",
        ["Security ,Madical facility ,play groud ,24 hr electricity ,etc"]
    ],

    [
        r"(.*)recently held events(.*)",
        ["ted x , maitree , milan , srijan ,  Battle of Dance"]
    ],

    [
        r"(.*)rules and Regulations of GLA University(.*)",
        ["Intentionally damaging property and equipment of the hostel,Gambling in Any Form is not allowed"]
    ],

    [
        r"(.*)academic Coucil(.*)",
        ["Vice Chancellor Prof. A.M. Agrawal Dean Prof. A. Pradhan Director Prof. Anoop Kumar Gupta"]
    ],

    [
        r"(.*)areas of research(.*)",
        [
            "Image Processing and Computer Vision Intelligent Systems Information Retrieval Data Mining and Data Analytics"]
    ],

    [
        r"(.*)average placement(.*)",
        ["The average placement rate of G L A University is 80 to 85 %"]
    ],

    [
        r"(.*)entrepreneurship cell(.*)",
        [
            "At E-Cell G L AU members from various backgrounds and departments combine their meticulous talents to help the youth achieve their dreams"]
    ],

    [
        r"(.*)clubs of our College(.*)",
        ["There are different different clubs in our college such as natraj club, udaan , aashayein, abacus, ASME etc"]
    ],

    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"what is your name ?",
        ["My name is G L A Assistant and I know almost everything about G L A University"]
    ],
    [
        r"how are you?",
        ["I'm doing good\nHow about You ?", ]
    ],
    [
        r"sorry(.*)",
        ["Its alright", "Its OK, never mind", ]
    ],
    [
        r"i'm(.*)doing good",
        ["Nice to hear that", "Alright :)", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"(.*)age?",
        ["I'm a computer program dude\nSeriously you are asking me this?", ]

    ],
    [
        r"what(.*)want?",
        ["Make me an offer I can't refuse", ]

    ],
    [
        r"(.*)created?",
        ["Manali and Shiv created me using Python's NLTK library "]
    ],
    [
        r"how is weather in(.*)?",
        ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1",
         "Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.", ]
    ],
    [
        r"(.*)raining in(.*)",
        ["No rain since last week here in %2", "Damn its raining too much here in %2"]
    ],
    [
        r"how(.*)health(.*)",
        ["I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"quit",
        ["Bye bye take care It was nice talking to you See you soon "]
    ],
]

chat = Chat(pairs, reflections)
while 1:
    with sr.Microphone(device_index=1, sample_rate=48000, chunk_size=1024) as source:
        r.adjust_for_ambient_noise(source)
        print("Say Something")

        audio = r.listen(source)
    text = 'GLA University'
    try:
        text = r.recognize_google(audio)
        print("you said: " + text)
    except:
        print("Something error ")
    
    res = chat.respond(text)
    if not res:
        value = client.query(text)
        res = next(value.results).text
        
    print(res)    
    engine.say(res)
    engine.runAndWait()  ##chat.converse()
    if text in ('quit' ,'bye', 'goodbye'):
        break
