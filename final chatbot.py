from requests import request
from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse
from urllib.request import urlopen
from msg_parser import MsOxMessage

app = Flask(__name__)


@app.route('/mybot', methods=['POST'])
def bot():
    user_msg = request.values.get('Body', '').lower()
    bot_resp = MessagingResponse()
    msg = bot_resp.message()

    def mainmenu():
        msg.body("Hi there! Welcome to VIT-AP University"
                 "\nType 1 for VITEEE FAQ"
                 "\nType 2 to know about B.Com."
                 "\nType 3 to know about BBA Admisiion"
                 "\nType 4 to know about LAW School"
                 "\nType 5 for M.Sc."
                 "\nType 6 for B.Sc.- M.Sc. Data Science Dual Degree Program"
                 "\nType 0 to STOP")

    def viteefaq():
        msg.body('''
        1.General queries\n
        2.Admission related queries\n 
        3.VITEE related queries\n
        4.VITEEE Eligibility Related Queries\n
        5.VITEEE Ranking Related Queries\n
        6.Payment Transaction Related Queries\n
        7.Slot Booking Related Queries\n
        8.Scholarship Related Queries\n
        9.Hostel Related Queries\n
        10.Academics Related Queries\n
        11.NRI / Foreign Students Admission Related Queries\n
        12.Main Menu
        ''')

        def generalqueries():
            msg.body('''
            1. Where can I find the link to apply for the B.Tech Degree program, through the general category?\n
            2. Which branch in Engineering would have the best scope?\n
            3.Are candidates appearing for Improvement/Privately also eligible to apply for VITEEE?\n
            4. What is the cost of the VITEEE Application form?\n
            5. Where can I find the fee structure for various programmes?\n
            6. How many campuses does VIT have?\n
            7. Will I be offered the option of choosing my campus and program while filling application?\n
            8. What is the closing date for issue of applications?\n
            9. Main Menu\n
            10. Previous Menu
            ''')
            if '1' in user_msg:
                msg.body(
                    "The link to apply for the B.Tech programmes (General category) https://viteee.vit.ac.in/ is available on the website vit.ac.in")
            elif '2' in user_msg:
                msg.body(
                    "All Engineering branches have an equally good scope. Much depends on your passion for the program and your endeavour to excel.")
            elif '3' in user_msg:
                msg.body(
                    "'Yes'. They are eligible to apply for VITEEE and should produce their marks sheet at the time of counselling / admission.")
            elif '4' in user_msg:
                msg.body(
                    "Online application - https://viteee.vit.ac.in/ - Rs. 1250/-")
            elif '5' in user_msg:
                msg.body(
                    "Please follow the link https://vit.ac.in/admission/ug/fee-structure")
            elif '6' in user_msg:
                msg.body("Under VIT Group there are: VIT Vellore, VIT Chennai, VIT AP and VIT Bhopal. The first two come under Deemed to be University and VIT-AP and VIT-Bhopal are state private Universities.")
            elif '7' in user_msg:
                msg.body("'No' only at the time of counselling you would be offered the option of choosing your campus and a program. This would depend on the availability of the campus as per your rank in the order of merit.")
            elif '8' in user_msg:
                msg.body("Applications will be issued till end of 30th May 2023")
            elif '9' in user_msg:
                mainmenu()
            elif '10' in user_msg:
                viteefaq()
            else:
                msg.body("Please enter a valid response.")

        def admissionqueries():
            msg.body('''
            1. Does VIT offer admissions through Management quota?\n
            2. Is there lateral entry admission available for Diploma candidates?\n
            3. Previous menu
            4. Main menu''')
            if '1' in user_msg:
                msg.body('''
                There is no Management Quota in VIT. Admissions is purely based on the merit rank obtained in the VITEEE and for other Undergraduate programs, it is based on the merit of your XII/ Higher Secondary Boards by which you would be accordingly ranked.
                ''')
            elif '2' in user_msg:
                msg.body('''
                'No'. There is no lateral entry admission offered for B.Tech and UG Programmes. Diploma holders (10+3) are eligible for B.Sc. Multimedia and Animation, Visual Communication, Fashion Designing (Chennai) with an overall aggregate of 60%.
                ''')
            elif '3' in user_msg:
                viteefaq()
            elif '4' in user_msg:
                mainmenu()
            else:
                msg.body("Invalid response")

        def viteequeries():
            msg.body('''
            1. Is VITEEE mandatory or would merit of XII / Higher Secondary Board, JEE Main / SAT scores be considered for admission to the B.Tech. Degree Programme?\n
            2. What would be the syllabus and Question pattern (QP) for the VITEEE?\n
            3. Could I have some information on the VITEEE?\n
            4. Will VITEEE 2022 be held as scheduled, considering the fact that CBSE and State Board exams have been postponed owing to the recent pandemic?\n
            5. If a student has selected / allotted a particular branch of Engineering through counselling, in a selected campus, under a specific category, would it be possible to change the branch, campus or category later?\n
            6. What would be the valid ID proofs needed to be produced in the entrance examination hall, in addition to the E-admit card with photograph?\n
            7. Is there an option to 'Edit' the application form in web?\n
            8. How do I edit my application?\n
            9. What am I supposed to do if my PIN code is not found in my application?\n
            10. Previous menu\n
            11. Main menu
            ''')
            if '1' in user_msg:
                msg.body(
                    "'Yes' VITEEE is mandatory for admission to the B.Tech. Programme in VIT. Higher Secondary Board, JEE Main/ SAT scores will not be considered for admission to the B.Tech. Degree Programme.")
            elif '2' in user_msg:
                msg.body(
                    '''- Please visit the https://viteee.vit.ac.in/ link for the syllabus.
                       - The questions (MCQ) will primarily be from the State Board of Higher Secondary Education and the CBSE syllabus. Math's or Biology (40 questions), Physics (35 questions), Chemistry (35 questions), Aptitude (10 questions) and English (5 questions) in two and half examination without negative marking.''')
            elif '3' in user_msg:
                msg.body('''- 
                VIT Engineering Entrance Examination will be conducted between 30th June to 6th July 2022 CBT - Computer based test.
                - The duration of the Entrance Examination will be of 2 hours and 30 minutes
                - The details on the sessions and timings would be intimated before slot booking.''')
            elif '4' in user_msg:
                msg.body(
                    "VITEEE is most likely to be held as scheduled. Candidates ranked through merit of VITEEE could attend counselling but produce their XII Mark sheet later to qualify for admission.")
            elif '5' in user_msg:
                msg.body(
                    "It is most unlikely that a change could be accommodated, once allotted. There is no Sliding/ up gradation in category / change of campus option offered further to admission.")
            elif '6' in user_msg:
                msg.body(
                    "You could produce either your Aadhaar card / Driving license / PAN card / Passport / Voter ID card or else School ID card as original.")
            elif '7' in user_msg:
                msg.body("'Yes'. Once you complete the application form, you will be able to edit your application. (After making the payment and uploading your photo & Signature)")
            elif '8' in user_msg:
                msg.body("You will find the 'Edit' option on the left side of the screen at the application - download stage. (You would be able to edit all fields inclusive of test city and uploaded documents).")
            elif '9' in user_msg:
                msg.body(
                    "'PIN code' has been integrated in our Software / Kindly mail (ugadmission@vit.ac.in)")
            elif '10' in user_msg:
                viteefaq()
            elif '11' in user_msg:
                mainmenu()
            else:
                msg.body("Please enter a valid response.")

        def four():
            msg.body('''
            1. I have secured 62% overall in +2 examination, but 53.35% in PCM / PCB. In such case, am I eligible for admission?\n
            2. Is there a specific age limit to apply for VITEEE?\n
            3. I am an Indian but have completed my 10+2 system of Higher Secondary Education abroad. What would I enter under the 'Nationality' field in such case?\n
            4. Which Engineering stream would I be eligible to apply for if I opt for Physics, Chemistry and Biology?\n
            5. Previous menu
            6. Main menu''')
            if '1' in user_msg:
                msg.body(
                    "'No'. You should satisfy the eligibility criteria of obtaining a minimum aggregate of 55% in PCM /PCB for the B.Tech. Programme.")
            elif '2' in user_msg:
                msg.body(
                    "'Yes'. Candidates whose date of birth falls on or after 1st July 2000 are only eligible to apply for VITEEE - 2022.")
            elif '3' in user_msg:
                msg.body(
                    "NRI (Non Resident Indian)")
            elif '4' in user_msg:
                msg.body('''
                If you have opted for Physics, Chemistry and Biology in the qualifying examination, you would be eligible only for
                B.Tech Bio-Engineering
                B.Tech Biotechnology
                B.Tech Computer Science and Engineering with specialization in Bioinformatics
                B.Tech Computer Science and Engineering (Specialization in Health Informatics)
                However you would be required to register for Mathematics as bridge course, which is mandatory''')
            elif '6' in user_msg:
                mainmenu()
            elif '5' in user_msg:
                viteefaq()
            else:
                msg.body("Please enter a valid response.")

        def five():
            msg.body('''
            1. What's the cut off / rank in VITEEE required for my desirable course?\n
            2. What should be the VITEEE preparation strategies?\n
            3. When will be the mock exam for VITEEE?\n
            4. Marking Scheme of VITEEE ranking?\n
            5. Previous menu\n
            6. Main menu''')
            if '1' in user_msg:
                msg.body("Admissions for B.Tech Branches are based on the merit rank from VITEEE and therefore it differs from year to year. It is only after you are ranked from the VITEEE and attend counselling that you may tentatively guess the rank range required for a particular branch. Higher the rank higher the chances to get your desirable course.")
            elif '2' in user_msg:
                msg.body('''
                VITEEE, like other competitive exams, requires proper strategy combined with excellent accuracy and speed. Although there is no negative marking like in other competitive examinations, you still need to have clear concepts and develop effective time-management strategies. Some preparation strategies that you can create are:\n
                1.	Time Management: For VITEEE exam, it is not necessary to solve all questions, but it is about solving decent number of questions in a proper time frame. If you are not able to solve any question, then please do not waste your time on it and move on to the next one. Also, it is advisable to attempt the easy questions first and gradually move towards attempting the difficult ones.\n
                2.	Develop Speed & Accuracy: Try to develop your own strategies to crack the exam. Enhance your analytical skills and aim to attempt all the questions while practicing. This will give you an edge over the other students.\n
                3.	Have Clear Concepts: Try to clear all your confusion on time, as it is important for you to have a strong foundation to solve all levels of questions. The more you practice, the easier it becomes for you to fine-tune your concepts. Apart from solving old VITEEE papers, you can also solve the NCERT books for classes 11 and 12.\n
                4.	Prepare Notes: It is advisable to prepare notes on the tips that you receive for the VITEEE exam. This will help you a lot during last minute revision, and the information might be handy for you, as you don't have to look through your books again and again.\n
                5.	Revision: Guess this is self-explanatory. You need to keep revising every few days to ensure the subject matter gets stored in your memory permanently.''')
            elif '3' in user_msg:
                msg.body("Mock test will be scheduled after slot booking.")
            elif '4' in user_msg:
                msg.body(
                    "Each question contains one mark; there is no negative marking for incorrect answers.")
            elif '5' in user_msg:
                viteefaq()
            elif '6' in user_msg:
                mainmenu()
            else:
                msg.body("Please enter a valid response.")

        def six():
            msg.body('''
            1.. What do I do if I have made the payment but not received a confirmation?\n
            2. Would there be a refund if I have made two payment transactions for my VITEEE application?\n
            3. What If I haven't received within 5-7 working days?\n
            4. Where could I find information about the 'Test cities'?\n
            5. Previous menu\n
            6. Main menu''')
            if '1' in user_msg:
                msg.body(''' 
                Please read this important instruction related to payment issues given below and also in the VITEEE page.\n
                - At the time of transaction, the amount is debited, kindly wait for an hour in the same login page.\n
                - If Amount debited more than one time, it will be refunded to your account in 5 to 7 days.''')
            elif '2' in user_msg:
                msg.body("'Yes'. If the amount towards the VITEEE application form has been paid twice for the same application, the excess amount paid will be refunded to your account within 7 working days.")
            elif '3' in user_msg:
                msg.body("You will be receiving within 5-7 working days; it's depending on the source through which the transaction was made. If not, you can connect with ugadmission@vit.ac.in / 0416 220 2020.")
            elif '4' in user_msg:
                msg.body("Please visit the link https://vit.ac.in/testcities")
            elif '5' in user_msg:
                viteefaq()
            elif '6' in user_msg:
                mainmenu()
            else:
                msg.body("Invalid response")

        def seven():
            msg.body(''' 
            1. How can I get the admit card?\n
            2. What is slot booking in VIT?\n
            3. Can student change their slots?\n
            4. Can student change their Test city?\n
            5. If student missed the slot booking, can he still apply?\n
            6. What was the last year's intake for B.Tech?\n
            7. Previous menu\n
            8. Main menu''')
            if '1' in user_msg:
                msg.body(
                    "After the slot booking, you would be able to download the admit card.")
            elif '2' in user_msg:
                msg.body("Slot booking refers to you choosing your venue, date and time for the VITEEE at your desired test city. VIT University starts the online VITEEE Slot Booking at VIT's Online Test Booking System (OTBS). The candidates have to use their VITEEE 2022 application number and password to enter the VIT OTBS. The slot booking is done in the first come first serve basis. After the VITEEE 2022 Slot booking the candidates can check their admit card that is generated just after. The candidates have to download the same and complete the process.")
            elif '3' in user_msg:
                msg.body("A slot once booked cannot be changed.")
            elif '4' in user_msg:
                msg.body(''''
                Yes' Can be changed till the application close for VITEEE 2022.\n 
                         •	Change of test city from abroad to India - No extra payment.\n
                         •	Change of test city from India to abroad - $50 Extra payment (OR equivalent INR).''')
            elif '5' in user_msg:
                msg.body("It is the responsibility of the candidates to book their test schedule in OTBS within the given time frame. The Institute will not be held accountable for the non-bookings. The application fee will not be refunded under any circumstances for such cases.")
            elif '6' in user_msg:
                msg.body("Admissions to various B.Tech Branches are based on the merit rank from VITEEE and therefore differ from year to year. It is only after you are ranked from the VITEEE and attends counselling that you could briefly estimate the rank range required for a particular branch. Do not believe any social media sources as they might mislead you.")
            elif '7' in user_msg:
                viteefaq()
            elif '8' in user_msg:
                mainmenu()
            else:
                msg.body("Invalid response")

        def eight():
            msg.body('''
            1. Does VIT provide scholarships to VITEEE meritorious students?\n
            2. Does VIT provide scholarships to students from rural areas and underprivileged meritorious students?\n
            3. Previous menu\n
            4. Main menu''')
            if '1' in user_msg:
                msg.body('''
                \nPerformance	                         Scholarship
                \nCentral and State Board Toppers	     100% waiver on Tuition Fees (for all 4 years)
                \n1 to 50 Rank Holder in VITEEE	     75% waiver on Tuition Fees (for all 4 years)
                \n51 to 100 Rank Holder in VITEEE	     50% waiver on Tuition Fees (for all 4 years)
                \n101 to 1000 Rank Holder in VITEEE	 25% waiver on Tuition Fees (for all 4 years)
                ''')
            elif '2' in user_msg:
                msg.body("STARS (Support the Advancement of Rural Students Scheme) helps students from under privileged backgrounds of Tamil Nadu/ Andhra Pradesh to achieve their dreams by giving them 100% fee waiver for their academic, hostel and basic medical expenses. Top boys and girls from Rural Government schools are shortlisted for the scheme.")
            elif '3' in user_msg:
                viteefaq()
            elif '4' in user_msg:
                mainmenu()
            else:
                msg.body("Invalid response")

        def nine():
            msg.body('''
            1. What is the hostel facilities offered on campus? \n
            2. Where can I find details on Hostel fees? \n
            3. Previous menu\n
            4. Main menu''')
            if '1' in user_msg:
                msg.body("Please visit the link: https://vitap.ac.in/hostels/")
            elif '2' in user_msg:
                msg.body(
                    "Please visit the link:  https://vitap.ac.in/ hostel-and-mess-fee-structure/ ")
            elif '3' in user_msg:
                viteefaq()
            elif '4' in user_msg:
                mainmenu()
            else:
                msg.body("Invalid response")

        def ten():
            msg.body(''' 
            1. Where can I find info on the M.Tech Integrated /PG programs?\n
            2. What are the other Undergraduate Degree programs offered in VITAP?\n
            3. What is Fully Flexible Credit System\n
            4. What is International Transfer Program (ITP)? Where can I get to know more?\n
            5. What is the Semester Abroad Program (SAP)?\n
            6. How are placements at VITAP?\n
            7. Previous menu\n
            8. Main menu ''')
            if '1' in user_msg:
                msg.body(
                    "Please visit the link: https://vitap.ac.in/ you could mail admission@vitap.ac.in or contact: 0863-2370444.")
            elif '2' in user_msg:
                msg.body(
                    "Please find details of Undergraduate programs offered in VIT at the link: https://vitap.ac.in/admission/overview ")
            elif '3' in user_msg:
                msg.body("In a Fully Flexible Credit System (FFCS), a candidate has the complete freedom to select time table with the choices on the teacher, time. In addition, they may register less or more number of courses (subject to minimum / maximum criteria) to finish early and take more than 6 month project in final year.")
            elif '4' in user_msg:
                msg.body("In an International Transfer program (ITP) - A student completes the first two years of his B.Tech Degree program in VIT and the next two years of his Degree at a partner university abroad. Call for ITP details 0863 2370444.")
            elif '5' in user_msg:
                msg.body("In a Semester Abroad program (SAP) - the student is provided an opportunity to pursue the final Semester in a partner university abroad. (Contact:  asstdir.ir@vitap.ac.in  for more details)")
            elif '6' in user_msg:
                msg.body(
                    "Please refer to the link: https://vitap.ac.in/ placement/career-development-centre/  ")
            elif '7' in user_msg:
                viteefaq()
            elif '8' in user_msg:
                mainmenu()
            else:
                msg.body("Invalid response")

        def eleven():
            msg.body('''
            i.	Indian passport holders whose parents are employed abroad can apply for both NRI as well as VITEEE (separate application and admission procedures).
            \nii.	PIO card holders can also apply for VITEEE but those holding only foreign passports are not eligible.
            \niii.	To know the admission procedure under NRI/ Foreign categories, kindly visit the below links.\n
            https://vit.ac.in/admissions/international/btech-eligibilityandprocedure   \n
            https://vit.ac.in/admissions/international/fee
            \niv.	For details on NRI admissions : nriadmission@vit.ac.in
            \nv.	For details on Foreign admissions: global@vit.ac.in ''')
            msg.body('''1. Previous menu
            2. Main menu''')
            if '1' in user_msg:
                viteefaq()
            elif '2' in user_msg:
                mainmenu()
            else:
                msg.body('Invalid input')
        if '1' in user_msg:
            generalqueries()
        elif '2' in user_msg:
            admissionqueries()
        elif '3' in user_msg:
            viteequeries()
        elif '4' in user_msg:
            four()
        elif '5' in user_msg:
            five()
        elif '6' in user_msg:
            six()
        elif '7' in user_msg:
            seven()
        elif '8' in user_msg:
            eight()
        elif '9' in user_msg:
            nine()
        elif '10' in user_msg:
            ten()
        elif '11' in user_msg:
            eleven()
        elif '12' in user_msg:
            mainmenu()
        else:
            msg.body("Invalid response")

    if 'hi' in user_msg:
        mainmenu()
    elif '1' in user_msg:
        viteefaq()
    elif '2' in user_msg:
        msg.body('''
        1. Can Science stream students pursue a B.Com ( Finance ) course in VIT-AP University?\n
        2. What is the minimum eligibility criteria for B. Com (Finance) ? Is Mathematics important for B.Com (Finance) ?\n
        3. What is the difference between B.Com and B.Com (Finance) course?\n
        4. Should I pursue B. Com (Finance) for Passing CA easily?\n
        5. What Subjects of CA Course You will be covering while pursuing B.Com (Finance) Course at VIT-AP University?
        ''')
        if "1" in user_msg:
            msg.body('''
            No. To pursue a B.Com (Finance) course, colleges require applicants to have studied and cleared Mathematics along with  Economic and Commerce (MEC) or Business Studies in the qualifying exam with at least 55% of Marks.
            ''')
        elif "2" in user_msg:
            msg.body('''
            The minimum eligibility criteria for B.Com (Finance)  course in VIT-AP University is to have cleared and qualified the class 12 board examination from a recognised board of education, such as CBSE, ICSE, State Education Boards or equivalent boards. For the second part of the question, as answered in the previous question, Mathematics is necessary for admissions to  the B.Com (Finance) course in VIT-AP University. Mathematics along with Economic and Commerce (MEC) or Business Studies in the qualifying exam with at least 55% of Marks.
            ''')
        elif "3" in user_msg:
            msg.body('''
            B.Com (Finance), students will be able to specialise in different fields such as Finance and Accounting, Banking, Insurance, Taxation, etc. The in-depth education and academic curriculum provide the students with a wider range of knowledge and expertise in commerce and banking. You will be able to pass CA, CS, CMA or CFA very easily if you study B.Com (Finance)
            On the other hand, B.Com as a course trains and produces qualified commerce graduates, capable of carrying day-to-day processes of commerce and banking. 
            ''')
        elif "4" in user_msg:
            msg.body('''
            Over the years, it has been a trend to see CA aspirants pursue B. Com (Finance) while also attempting to clear CA exams as well. At VIT-AP we will prepare you for CA-Foundation and CA-Inter as well while studying B. Com (Finance) at VIT-AP Campus.
            ''')
        elif "5" in user_msg:
            msg.body('''
            The Following Subjects of CA Course will be covered while Pursuing B.Com (Finance)
            CA Subjects in CA Foundation Course or CPT (Common Proficiency Test)
            1.	Fundamentals of Accounting
            2.	Quantitative aptitude
            3.	Mercantile Law
            4.	General Economics
            5.	General English
            CA Subjects in Intermediate Course or IPCC (Integrated Professional Competence Course)
            1.	Accounting
            2.	Cost Accounting and Financial Management
            3.	Advanced Accounting
            4.	Taxation
            5.	Auditing and Assurance
            6.	Business Laws, Ethics and Communication
            7.	Information Technology and Strategic Management
            8.	Corporate and other Laws
            CA Final Subjects
            1.	Advanced Auditing and Professional Ethics
            2.	Financial Reporting
            3.	Strategic Financial Management
            4.	Strategic Cost Management and Performance Evaluation
            5.	Corporate and Economic Laws
            6.	Direct Tax Laws and International Taxation
            7.	Indirect Tax Laws
            There are also electives from which students can choose one.
            1.	Risk Management
            2.	International Taxation
            3.	Economic Laws
            4.	Financial Services and Capital Markets
            5.	Global Financial Reporting Standards
            6.	Multidisciplinary Case Studies
            CA Final Group 1 Subjects
            1.	Financial Reporting
            2.	Strategic Financial Management
            3.	Advanced Auditing and Professional Ethics
            4.	Corporate and Allied Laws
            CA Final Group 2 Subjects
            1.	Advanced Management Accounting
            2.	Information systems Control and Audit
            3.	Direct Tax Laws
            4.	Indirect Tax Laws
            CA Final Subjects (Extracted from New Course Syllabus)
            1.	Financial Reporting
            2.	Strategic Financial Management
            3.	Advanced Auditing and Professional Ethics
            4.	Corporate and Economic Laws
            5.	Strategic Cost Management and Performance Evaluation
            6.	Direct Tax Laws and International Taxation
            7.	Indirect Tax Laws ''')
        else:
            msg.body('''Enter a valid resposne''')

    elif '3' in user_msg:
        msg.body('''
       1. BBA program\n
       2. Admisiion details\n
       3. International collaboration
       ''')
        if '1' in user_msg:
            user_msg('''
        1.	What is BBA Program?\n
        2.  What are the different programmes under BBA?\n
        3.  What are Specialisations in BBA?\n
        4.  What is Business Analytics?\n
        5.	Why should I choose Business Analytics?\n
        6.	 What is unique about the BBA Curriculum?\n
        ''')
            if '1' in user_msg:
                msg.body('''VIT-AP School of Business (VSB) builds on VIT’s long history of excellence in technical education with liberal arts and humanities, topped with best of the management courses, to offer a world class BBA (Bachelor of Business Administration) program. VSB believes that every manager should be strongly grounded in the fundamentals of management, thus, the BBA programme is designed to provide breadth and suitable depth with well-designed curriculum built on the liberal education foundation and exposure to engineering and technology. The BBA programme consists of courses designed in collaboration with industry experts and academicians from IIMs and international universities.
                         Students can choose Business Analytics, Digital Marketing, Fintech or General Management as specialisation. As part of the specialisation, students will undergo practice oriented skill building courses leading to certifications in Business Analytics, Digital Marketing or Fintech.
                         VSB has International Credit Transfer Agreements with University of Michigan, Dearborn, USA (UMD) and Arizona State University, USA (ASU) leading to BBA from UMD and BS Business Data Analytics from ASU.
                         ''')
            elif '2' in user_msg:
                msg.body('''The school offers the following programmes-
                         •	BBA (Specialization in Business Analytics, Digital Marketing, Fintech, General Management)
                         •	BBA from University of Michigan, Dearborn (UMD), USA - 2 years at VSB + 2 years at UMD (Majors in Accounting, Digital Marketing, Finance, HRM, IS Management, Marketing and Supply Chain Management)
                         •	BS Business Analytics ''')
            elif '3' in user_msg:
                msg.body('''A student joining BBA program in VSB can choose any of the following specialisations after the completion of first year.
                         BBA with specialisation in Business Analytics
                         BBA with specialisation in Digital Marketing
                         BBA with specialisation in FinTech
                         BBA with specialisation in General Management
                         ''')
            elif '4' in user_msg:
                msg.body('''A: Business Analytics is a field that drives data-driven decisions-making in the businesses. It is the practical application of statistical techniques that focuses on providing actionable recommendations to the businesses based on data. It harnesses the power of information technology to process and analyse ever-increasing amounts of data available to businesses. Business Analytics as a field requires skills and competencies in the domains of business & management; mathematics & statistics, and IT & computer science''')
            elif '5' in user_msg:
                msg.body('''
                A: You should choose Business Analytics, if
                *	You have a flare for numbers and data,
                *	You are comfortable with Mathematics and Statistics,
                *	You like working with Information Technology and have interest in the latest developments in Computer Science,
                *	You are comfortable working with latest tools and technologies available in the market,
                *	You like to do coding and programming in various programming languages.
                ''')
            elif '6' in user_msg:
                msg.body('''
                Liberal Arts Courses– Anthropology / Sociology, Psychology / Social Psychology, Theatre and Literature.
                Critical thinking – How to think
                STEM Courses – Environmental Studies, Physics, Chemistry, Mathematics, Statistics, Python, Mechanical Workshop.
                Unique Courses – Ethics & Values, Systems Thinking & Dynamics and Design Thinking & Innovation. All BBA students will have the option of joining Discovering Self and Globalisation and Culture workshops (highly acclaimed courses from IIM Kozhikode).
                Other than these innovative workshops are planned every semester on culture, development, ecology, economy, gender, global issues, innovations, rural India, start-ups, technology, theatre and so on.
                Field work every year– Students will go on field work on variety of themes such as a. Cultures of India, b. Appreciating Rural India, c. Heritage and Current Social Reality, or d. Dynamics of Entrepreneurship.
                ''')
            else:
                msg.body("Invalid response")
        elif '2' in user_msg:
            msg.body('''
            1.	What is the Admission Process\n
            2.	 What is the eligibility criteria for each program?\n
            3.  What are important dates related to BBA admission 2022?\n
            4.  How to apply?\n
            5.	What is the Merit Scholarships?\n
            6.	Fees\n
            7.	What are the career opportunities after BBA ?\n
            ''')
            if '1' in user_msg:
                msg.body('''
                Step 1 – Apply Online https://vit.ac.in
                Step 2 – Attend Personal Interview – eligible candidates will be informed by email
                Step 3 – Merit List & Scholarships will be announced – Students pay full academic fees within last date and take provisional admission.
                Step 4 – If hostel accommodation is required, apply and make an online payment for Hostel+Mess fees
                Step 5 – Join VSB on the specified date for joining formalities and orientation program (date to be announced)
                ''')
            elif '2' in user_msg:
                msg.media(
                    'https://vitapacin-my.sharepoint.com/:i:/g/personal/krishna_21bce8114_vitapstudent_ac_in/EdF32EM1WvtOgl1Nx69q8xIBYlPAhxB5-3HktS7LjWvYgg?e=C0YOeo')
            elif '3' in user_msg:
                msg.body('''
                Last date for BBA Applications – 30th June 2023
                ''')
            elif '4' in user_msg:
                msg.body('''
                Register online to apply – https://vit.ac.in
                You will get login id and password in registered email and mobile number
                Log in, change the password and fill in all the required details and upload scanned copies of 10th and 12th Std. Mark sheets. Submit the form. Make a payment of Rs 500 for application fees
                Eligible candidates will be informed about the Management Test by email.
                ''')
            elif '5' in user_msg:
                msg.body('''
                We have created merit scholarships, which reduces the academic fees substantially. The various categories of the scholarships and the Academic Fees payable are given below. A merit list will be created based on the 12th marks and performance in Personal              Interview (PI). Co-curricular and extra-curricular achievements at the state and above levels will also be given consideration. Only selected candidates will be considered for scholarships.\n\n
                ''')
                msg.media(
                    'https://vitapacin-my.sharepoint.com/:i:/g/personal/krishna_21bce8114_vitapstudent_ac_in/Eb0t4V3iwcdMoCP9pWbRvicBSyzH3vI20bRbwT-hyE2ZCA?e=rN7cus')
            elif '6' in user_msg:
                msg.body('''
                Tuition Fees (Per Annum)	INR 2,72,000
                Caution Deposit (Refundable) (One time payment) INR 3,000 Total fees to be paid for the first year INR 2,75,000
                Hostel & Mess Fees – We suggest all BBA students to enroll in the hostel, to fully benefit from the curriculum. The hostel+mess fees will be intimated shortly. 
                ''')
                msg.media(
                    'https://vitapacin-my.sharepoint.com/:i:/g/personal/krishna_21bce8114_vitapstudent_ac_in/ESB8kdCeZx5CpxLmvUS271oBbo76ko5xi9C91MX6sxMOTQ?e=YFUtwh')
            elif '7' in user_msg:
                msg.body('''
                BBA students have great opportunities in the Indian corporates, start their own business or join the family business. Startup incubation support is given by the university. Industry recognised certifications will give VSB students a competitive advantage over others in the Job Market.
                Students aspiring for to go for higher studies, join family business or start their own companies can go for specialisation in General Management 
                ''')
            else:
                msg.body("Invalid response")
        elif '3' in user_msg:
            msg.body('''
            1.	What is the Eligibility criteria BBA (All Specialisations)\n
            2.	Details about 2 + 2 BBA Program with University of Michigan, Dearborn (UMD), USA\n
            3.	 Details about 2+2 BS Business Analytics from Arizona State University (ASU), USA\n
            4.	What are the Key features of the program?\n
            5.	What are International Credit Transfer Programs\n
            ''')
            if '1' in user_msg:
                msg.body('''
                 Candidate should have born on or after 01.07.2002
                 Candidates who have studied in Regular, Full time and Formal Education are alone eligible to apply
                 60% aggregate or equivalent grades in 12th Std. Candidates studying 12th Std. in any group are eligible Candidates awaiting 12th Std. results can also apply.
                 *BBA @University of Michigan-Dearborn, USA*
                 Complete the BBA Prerequisite courses
                 Establish a minimum grade point average of 2.80 in a minimum of four upper level COB courses at UM-Dearborn, including at least one from FIN 401 or BE 401
                 Fulfill the writing requirement
                 English Language Proficiency: Minimum of 6.5 in IELTS or 80 in Internet-Based TOEFL
                 *BS Business Analytics @ Arizona State University, USA*
                 CGPA of 3.00 in the first two years coursework at VIT-AP
                 1160 (prior to March 2016) or 1230 SAT Reasoning (after March 2016), or 25 ACT score.
                 English Proficiency: Test of English as a Foreign Language (TOEFL): minimum 61(iBT), or International English Language Testing System (IELTS): minimum 6.0, or Pearson Test of English (PTE): minimum 53
                ''')
                msg.media(
                    'https://vitapacin-my.sharepoint.com/:i:/g/personal/krishna_21bce8114_vitapstudent_ac_in/EaK2x50KKfVIunm_Lp4WsZIBCtIv4lrfyzAyzeh2YLfYEg?e=jWCvq1')
            elif '2' in user_msg:
                msg.body('''
                1. 2+2 BBA from UMD\n
                2. Fee details\n
                3. Details about partenership of VIT-AP and UMD\n
                4. Details about specializations available at UMD\n
                ''')
                if '1' in user_msg:
                    msg.boudy('https://vit.ac.in')
                elif '2' in user_msg:
                    msg.boudy('https://vit.ac.in')
                elif '3' in user_msg:
                    msg.boudy('https://vit.ac.in')
                elif '4' in user_msg:
                    msg.boudy('https://vit.ac.in')
            elif '3' in user_msg:
                msg.body('''
                1.Details about BS Business Analytics degree from ASU and career options\n
                2.Details about VIT-AP and ASU tie-up\n
                3.Details about fees at ASU\n
                ''')
                if '1' in user_msg:
                    msg.boudy('https://vit.ac.in')
                elif '2' in user_msg:
                    msg.boudy('https://vit.ac.in')
                elif '3' in user_msg:
                    msg.boudy('https://vit.ac.in')
            elif '4' in user_msg:
                msg.body('''
                •	Industry recognised certification
                •	Co-Opt project during the 6th Semester Curriculum benchmarked against US Universities
                •	Liberal Arts Foundation + Exposure to Technology Visiting faculty from US Universities and IIMs
                ''')
            elif '5' in user_msg:
                msg.body('''
                Students can opt for a degree from our partner university in USA. The student will have to fulfil the requirements of the partnering university and may have to take additional courses during the summer semesters.
                Student opting for 2+2 UMD and ASU program need to inform after first semester
                BBA from University of Michigan, Dearborn (UMD): 2 years at VSB + 2 years at UMD https://vit.ac.in
                BS Business Analytics from Arizona State University (ASU): 2 years at VSB + 2 years at ASU https://vit.ac.in
                University of Michigan Dearborn offers the following Majors in their BBA program https://vit.ac.in
                ''')
            else:
                msg.body("Invalid response")

                msg.body("Invalid response")

    elif '4' in user_msg:
        msg.body('''
        1. Where is the VIT-AP campus located?  Is VIT-AP University recognised by the UGC? \n
        2. What is unique about the curriculum offered by VIT-AP University School of Law (VSL)?\n
        3. What are the courses offered at VSL? Is VIT-AP University School of Law (VSL) recognised by the Bar Council of India (BCI)? \n
        4. What is the faculty strength of VSL?\n
        5. What is the admission procedure for the BA, LL.B (Hons) and BBA, program?\n
        6. Are courses like BA, LL. B (Hons) and BBA, LL. B (Hons) part of the residential program?\n
        7. How are the hostel facilities on VIT-AP campus?  \n
        8. Are placements provided by the University?\n
        ''')
        if '1' in user_msg:
            msg.body('''The campus is located at Inavolu, Amaravathi which is about 2 kms from the Secretariat of Andhra Pradesh. 
                     Yes, VIT-AP University at Amaravati is a private university established in 2017 by the Andhra Pradesh Private University Act of 2016. It is recognised and approved by the University Grants Commission (UGC). ''')
        elif '2' in user_msg:
            msg.body('''The course curriculum is interdisciplinary and is designed to make students industry ready and  cater to the needs of global legal fraternity. The curriculum is carefully designed in consultation with the industry experts and renowned academics in the legal field.  BBA and LL. B (Hons) give opportunities to the students to opt for the legal subjects which are of contemporary relevance. Students can choose subjects from the wide range of core, honours, optional, electives and seminar courses. Each course is designed to have a research focus. ''')
        elif '3' in user_msg:
            msg.body('''At VSL, BBA., LL. B (Hons) and B.A., LL. B (Hons) Courses are available and a full time three years course ie., Ph.D. in Law. 
                     Yes, VIT-AP University School of Law (VSL) is recognised by the Bar Council of India (BCI) in 2019 
                     ''')
        elif '4' in user_msg:
            msg.body('''VSL possess faculties with international exposure and repute. They have expertise in a wide variety of subjects from which students can be benefited.  ''')
        elif '5' in user_msg:
            msg.body('''Admissions are as per the norms of the Bar Council of India (BCI). Students must have completed the 10+2 or Intermediate or PUC or equivalent examination from any recognised board. Students will be admitted based on VSLAT (GD / PI). LSAT/ CLAT score will also be taken into consideration for admission.''')
        elif '6' in user_msg:
            msg.body('''Yes, the courses mentioned are part of the residential program and students are expected to stay in the campus. However, in special circumstances students may be permitted to commute from their homes, if students are from within the travel distance.''')
        elif '7' in user_msg:
            msg.body('''VIT-AP University provides residential accommodation keeping in mind the comfort of the students. As per the budget requirements, they can choose the accommodation. ''')
        elif '8' in user_msg:
            msg.body('''Yes, the university may assist students in getting internships and placements at reputed legal firms in India and abroad with the office of the Senior Advocates at High Courts and Supreme Court, Research Organisations, NGOs, Media Houses and international and national organisations. A qualified and designated person will guide students in the internship and placement processes. ''')

    elif '5' in user_msg:
        msg.body('''
        1.	M. Sc. Physics\n
        2.	M. Sc. Chemistry\n
        3.	M. Sc. Data Science\n
        4.	Main Menu ''')
        if '1' in user_msg:
            msg.body('''
            1.	What is the eligibility criteria for the programme?\n
            2. When is the start date for the programme?\n
            3.  What is the duration of the programme?\n
            4.  Is there any research project opportunity available during the programme?\n
            5.  Is there any specialization offered?\n
            6.  What are the career opportunities in after obtaining the degree?\n
            ''')
            if '1' in user_msg:
                msg.body(
                    " Students with a Bachelor’s degree with minimum 60 % marks in Physics as major subject.")
            elif '2' in user_msg:
                msg.body("Fall semester (starting July/August) 2022")
            elif '3' in user_msg:
                msg.body("2 years (4 semesters)")
            elif '4' in user_msg:
                msg.body("The M.Sc. Physics programme includes a final semester project work within the department. Also, there is an interim Science, Engineering and Technology project that students could engage in.")
            elif '5' in user_msg:
                msg.body(
                    "There are specializations offered in various subjects, having relevance in frontline industry and research.")
            elif '6' in user_msg:
                msg.body('''
                There are multiple career opportunities upon completion of degree. They are categorized below: \n
                1. Research positions\n
                Degree holders could get into Ph.D. programmes at national and international institutes or Universities.
                Research scientist positions are also available for M.Sc. Physics graduates in premier organizations such as BARC, ISRO and DRDO, and other organizations in the Research & Development sectors.\n 
                2. Teaching positions\n
                Degree holders are eligible to be appointed as lecturers in colleges all across India.\n
                3. In industry\n
                Degree holders could get into electronics, instrumentation, materials and manufacturing industry depending on their specialization. They could also join in as scientific assistants in forensic laboratories, and scientific advisors in various organizations.
                ''')
            else:
                msg.body("Invalid response")
        elif '2' in user_msg:
            msg.body('''
            1. Application/ Admission\n
            2. fee and accomodation''')
            if '1' in user_msg:
                msg.body('''
                1.	What are the entry requirements for the MSc programmes offered by the Department of Chemistry?\n
                2.	Am I eligible to apply?\n
                3.	Which programme is most suitable for my profile?\n
                4.	How do I apply? \n
                5.	Where can I get help with the application process?\n
                6. 	When should I submit my application?\n
                7.  What should my application include?\n
                8.	Do I need to write VIT-AP University entrance exam?\n
                9.	If I am still undertaking a degree, can I apply to your MSc?\n
                10.	Do I need to submit a transcript at the time of applying for MSc?\n
                11.	How can I check the progress of my application?\n
                12.	How will I get the final decision on my application?\n                
                ''')
                if '1' in user_msg:
                    msg.body(
                        "A pass in BSc, with Chemistry as one of the subjects and with an overall pass percentage of 50% marks.")
                elif '2' in user_msg:
                    msg.body("Yes. A candidate who passed BSc degree OR studying in the final semester, with Chemistry as one of the subjects and with an overall pass percentage of 50% marks.")
                elif '3' in user_msg:
                    msg.body("Our VIT-AP University offers PG level programmes at present in various science disciplines (Maths, Physics and Chemistry) You can select based on your area of interest.")
                elif '5' in user_msg:
                    # to add contact
                    msg.body(
                        "(Our Admission Office contact numbers may be provided here).")
                elif '4' in user_msg:
                    msg.body(
                        "The application process will be in online mode. Please refer regularly our website (www.vitap.ac.in) for application process details and updates, if any.")
                elif '6' in user_msg:
                    msg.body(
                        "By online mode as per the format given. (Submitting in person may also be considered by Admission Office).")
                elif '7' in user_msg:
                    msg.body(
                        "Fill your application in the given format and also attach the required documents as requested in the application form.")
                elif '8' in user_msg:
                    msg.body(
                        "(At present, NO entrance exam by VIT-AP University. Admission Office may provide correct information).")
                elif '9' in user_msg:
                    msg.body(
                        "Yes. A candidate studying in the final semester of BSc degree, with Chemistry as one of the subjects can apply.")
                elif '10' in user_msg:
                    msg.body(
                        "For applying, a transcript is not required. During counselling process, you need to submit all the transcripts.")
                elif '11' in user_msg:
                    msg.body(
                        "You can check by logging into the VIT-AP University website with your application username and password.")
                elif '12' in user_msg:
                    msg.body(
                        "You can check by logging into the VIT-AP University website with your application username and password.")
                else:
                    msg.body("Invalid response")
            elif '2' in user_msg:
                msg.body(''' 
                1.	How much does it cost to study MSc Chemistry at VIT-AP University?\n
                2.	How do I apply for accommodation?\n
                3.	Where can I see the structure and courses of each programme?\n
                4.	Can I study the MSc part-time?\n
                5.	I have a question about the programme content/structure which is not answered on the website. Who can I contact with my query?\n
                6.	Where do the MSc Chemistry students go after course completion?\n
                7.	Are the Department’s MSc programmes a suitable route to top PhD programmes?\n
                8.	Can I automatically progress from the MSc Chemistry to the PhD programme in VIT-AP University?\n
                ''')
                if '1' in user_msg:
                    msg.body(
                        "(Depends. Day scholar or Hosteller. Admission Office may provide correct answer)")
                elif '2' in user_msg:
                    msg.body(
                        "Once you got selected, you can apply for hostel accommodation by online mode.")
                elif '3' in user_msg:
                    msg.body("Kindly refer our VIT-AP University website.")
                elif '4' in user_msg:
                    msg.body("At present full-time programmes only offered.")
                elif '5' in user_msg:
                    msg.body(
                        "You are most welcome to contact our Admission Office and you will be guided accordingly.")
                elif '6' in user_msg:
                    msg.body(
                        "For higher studies such as PhD in reputed institutions and also job opportunities in many industries.")
                elif '7' in user_msg:
                    msg.body(
                        "Yes. The PG programme is structured in such a way for having good chances to get admissions in reputed institutions.")
                elif '8' in user_msg:
                    msg.body(
                        "You can apply for PhD admission in VIT-AP University.")
                else:
                    msg.body("Invalid response")
        elif '3' in user_msg:
            msg.body('''
            1.	General Information:\n
            2.	Program Information:\n
            3.	Eligibility and Admissions:\n
            4.	Choosing Courses:\n
            5.	Finances:\n
            6.	Careers in Data Science:\n
            7.  main menu
            ''')
            if '1' in user_msg:
                msg.body('''
                1.	Is there any hostel facility in VIT-AP?\n
                2.	Is there any transportation facility for students?\n
                3.	Can I visit the campus to know more about the program and University?\n
                4.	Where to look to know more information about the Program and the corresponding school?
                ''')
                if '1' in user_msg:
                    msg.body(
                        " Yes, VIT-AP provides highly secure and well-guarded hostel facility separately for boys and girls. For more details visit https://vitap.ac.in/hostels/")
                elif '2' in user_msg:
                    msg.body(" Yes, VIT-AP provides bus transportation facility for the day scholar students. The buses are safe, secure, and driven by responsible personnel. Day scholars can avail the bus facility from Vijayawada, Guntur, and Tenali. For more details visit https://vitap.ac.in/transport/")
                elif '3' in user_msg:
                    msg.body(
                        "Yes, you are welcome to visit the University to get to know more about the program and the University.")
                elif '4' in user_msg:
                    msg.body(
                        "Refer the School website: http://vitap.ac.in/school-of-advanced-sciences/")
                else:
                    msg.body("Invalid response")
            elif '2' in user_msg:
                msg.body('''
                1.	What is data Science?\n
                2.	Why is it important to join this program?
                ''')
                if '1' in user_msg:
                    msg.body("Data Science is a multi- disciplinary field that uses scientific methods, processes, algorithms to produce knowledge & insights from structured & unstructured data. It utilises techniques & theories derived from many fields such as computer science, mathematics, statistics & information science to process and analyse large amount of data, and to present the results to reveal patterns and enable stakeholders to draw informed conclusions")
                elif '2' in user_msg:
                    msg.body("The technological advances used to be mostly driven by improved hardware that increased processing power, but also impelled physical limitations, therefore, the focus has now been shifting to software-driven applications. Data, the oil of the digital economy as it is called, is expected fuel our future. With the increase of computing power and digital storage come many new possibilities that - just ten to fifteen years ago - were beyond our imagination. Such new developments led to an increased demand for Data Scientist not just in IT sector but also in sectors such as banking and finance, automotive, energy, healthcare, transport, retail, and virtually every domain you can think of. Data has already started driving business decisions - from small regional offices to the boardroom – and hence graduates from study programmes in Data Science will be directly involved in important strategic decision-making processes. The program is designed to create knowledge pool that can address the ever-growing demand and challenges for experts in this field.")
                else:
                    msg.body("Invalid response")
            elif '3' in user_msg:
                msg.body('''
                1.	What are the eligibility criteria for admission into this program?\n
                2.	When will the application process for admission to this program start?\n
                3.	What is the closing date for issue of applications?\n
                4.	When and how can I apply?
                ''')
                if '1' in user_msg:
                    msg.body("Undergraduate degree in Mathematics/Statistics/Computer Science/Computer Applications/Data Science or UG Degree in Engineering or Technology in CSE/IT/ECE/EEE/E&I with a 60% of marks (Inclusive of all subjects).")
                elif '2' in user_msg:
                    msg.body(
                        "The admission process has already started, for more details contact The Admissions Office, or refer https://vitap.ac.in/contact-us/")
                elif '3' in user_msg:
                    msg.body(
                        "You may contact the VIT-AP University Admissions Office.")
                elif '4' in user_msg:
                    msg.body(
                        "The M. Sc Data Science program uses the online application for the VIT-AP University. Please refer to the University Website. ")
                else:
                    msg.body("Invalid response")
            elif '4' in user_msg:
                msg.body('''
                1.	What are the important courses offered in this program?\n
                2.	Does the curriculum provide industry internship or project-based learning opportunities?
                ''')
                if '1' in user_msg:
                    msg.body("The curriculum is designed in such a way that graduating students will be industry ready. The study of data science is constituted with the knowledge of mathematics, statistics, and computer science. The proposed program specialization will help students acquire the knowledge about industry relevant skills on Mathematical modeling, statistical modeling, data science concepts, machine learning principles and algorithms and visualization techniques.")
                elif '2' in user_msg:
                    msg.body("The curriculum has scope for all the advanced teaching-learning methodologies such as application-oriented and project-based learning and industry internships. ")
                else:
                    msg.body("Invalid response")
            elif '5' in user_msg:
                msg.body('''
                1.	What is the fee structure for this program?\n
                2.	Are there any scholarships provided?
                ''')
                if '1' in user_msg:
                    msg.body("Contact Admissions Office, VIT-AP University.")
                elif '2' in user_msg:
                    msg.body(
                        "VIT-AP University provides scholarships for meritorious students based on assessment.")
                else:
                    msg.body("Invalid response")
            elif '6' in user_msg:
                msg.body('''
                1.	What are the career opportunities for the graduates of this program?\n
                2.	Does VIT-AP offer Campus placement facilities? ''')
                if '1' in user_msg:
                    msg.body('''
                    This Inter-disciplinary program brings together a lot of skills required by Data Scientists with adequate domain knowledge to help any organization find ways to take major business decisions, reduce costs, get into new markets, launch a new product or service, find the sentiment of the customers, so on. The following industries/sectors would be the expected employers.
                    •	IT industries
                    •	Research institutions 
                    •	Banking sector
                    •	Consulting firms
                    •	Pharmaceutical companies
                    •	Automobile industries and 
                    •	Finance
                    •	Educational sector''')
                elif '2' in user_msg:
                    msg.body(
                        "VIT Provides centralized campus placements throughout all the VIT Campuses. ")
                else:
                    msg.body("Invalid response")
            elif '7' in user_msg:
                msg.body("main many")
            else:
                msg.body("Invalid response")

    elif '6' in user_msg:
        msg.body('''
        1. General Information:\n
        2.	Program Information:\n
        3.	Eligibility and Admissions:\n
        4.	Choosing Courses:\n
        5.	Finances:\n
        6. Careers in Data Science:
        ''')
        if '1' in user_msg:
            msg.body('''
            1.	Is there any hostel facility in VIT-AP?\n
            2.	Is there any transportation facility for students?\n
            3.	Can I visit the campus to know more about the program and University?\n
            4.	Where to look to know more information about the Program and the corresponding school?
            ''')
            if '1' in user_msg:
                msg.body("Yes, VIT-AP provides highly secure and well-guarded hostel facility separately for boys and girls. For more details visit https://vitap.ac.in/hostels/ ")
            elif '2' in user_msg:
                msg.body("Yes, VIT-AP provides bus transportation facility for the day scholar students. The buses are safe, secure, and driven by responsible personnel. Day scholars can avail the bus facility from Vijayawada, Guntur, and Tenali. For more details visit https://vitap.ac.in/transport/ ")
            elif '3' in user_msg:
                msg.body(
                    "Yes, you are welcome to visit the University to get to know more about the program and the University.")
            elif '4' in user_msg:
                msg.body(
                    "Refer the School website: http://vitap.ac.in/school-of-advanced-sciences/")
            else:
                msg.body("Invalid response")
        elif '2' in user_msg:
            msg.body(''' 
            1. What is data Science?\n
            2. Why is it important to join this program?
            ''')
            if '1' in user_msg:
                msg.body("Data Science is a multi- disciplinary field that uses scientific methods, processes, algorithms to produce knowledge & insights from structured & unstructured data. It utilises techniques & theories derived from many fields such as computer science, mathematics, statistics & information science to process and analyse large amount of data, and to present the results to reveal patterns and enable stakeholders to draw informed conclusions. ")
            elif '2' in user_msg:
                msg.body(" The technological advances used to be mostly driven by improved hardware that increased processing power, but also impelled physical limitations, therefore, the focus has now been shifting to software-driven applications. Data, the oil of the digital economy as it is called, is expected fuel our future. With the increase of computing power and digital storage come many new possibilities that - just ten to fifteen years ago - were beyond our imagination. Such new developments led to an increased demand for Data Scientist not just in IT sector but also in sectors such as banking and finance, automotive, energy, healthcare, transport, retail, and virtually every domain you can think of. Data has already started driving business decisions - from small regional offices to the boardroom – and hence graduates from study programmes in Data Science will be directly involved in important strategic decision-making processes. The program is designed to create knowledge pool that can address the ever-growing demand and challenges for experts in this field.")
            else:
                msg.body("Invalid response")
        elif '3' in user_msg:
            msg.body(''' 
            1. What are the eligibility criteria for admission into this program?'\n
            2. I have not studied Mathematics in my Intermediate or 10+2, can I apply for this program?\n
            3. What is meant by dual degree Program?\n
            4. What is exit option? When can I exercise it?\n
            5.	When will the application process for admission to this program start?\n
            6.	What is the closing date for issue of applications?\n
            7.	When and how can I apply?
            ''')
            if '1' in user_msg:
                msg.body('''
                • First Class with a minimum of 60% marks at 10+2 level /Intermediate/CBSE/ICSE/HSC/ or equivalent with Mathematics /Statistics /Computer Science/Business Mathematics as one of the subjects.
                • Age Limit: Date of Birth falls on or after 01.07.2000 (or any date based on the UG admission age limit)
                ''')
            elif '2' in user_msg:
                msg.body(
                    "Having studied Mathematics at Intermediate/10+2 level is essential prerequisite for joining this program. ")
            elif '3' in user_msg:
                msg.body("After 3 years of successful completion of this programme the B.Sc. degree in Data Science will be awarded irrespective of the students taking the exit option or not and on continuation with masters’ level study M.Sc. degree in Data Science will be awarded after successful completion of another 2 years.")
            elif '4' in user_msg:
                msg.body("After 3 years of successful completion of this programme, if a student gets a campus placement or he gets admission in masters at a partner university, or for some other reasons, if he wants to exit the program, he can do so with a B.Sc. degree in Data Science. ")
            elif '5' in user_msg:
                msg.body(
                    "The admission process has already started, for more details contact The Admissions Office, or refer https://vitap.ac.in/contact-us/")
            elif '6' in user_msg:
                msg.body(
                    "You may contact the VIT-AP University Admissions Office. ")
            elif '7' in user_msg:
                msg.body(
                    "The B Sc.& M. Sc Data Science program uses the online application for the VIT-AP University. Please refer to the University Website. ")
            else:
                msg.body("Invalid response")
        elif '4' in user_msg:
            msg.body(''' 
            1. What are the important courses offered in this program?\n
            2. Does the curriculum provide industry internship or project-based learning opportunities?
            ''')
            if '1' in user_msg:
                msg.body("The curriculum is designed in such a way that graduating students will be industry ready. The study of data science is constituted with the knowledge of mathematics, statistics, and computer science. The proposed program specialization will help students acquire the knowledge about industry relevant skills on Mathematical modeling, statistical modeling, data science concepts, machine learning principles and algorithms and visualization techniques. ")
            elif '2' in user_msg:
                msg.body("The curriculum has scope for all the advanced teaching-learning methodologies such as application-oriented and project-based learning and industry internships. ")
            else:
                msg.body("Invalid response")
        elif '5' in user_msg:
            msg.body(''' 
            1. What is the fee structure for this program?\n
            2. Are there any scholarships provided?''')
            if '1' in user_msg:
                msg.body("Contact Admissions Office, VIT-AP University.")
            elif '2' in user_msg:
                msg.body(
                    "VIT-AP University provides scholarships for meritorious students based on assessment. ")
            else:
                msg.body("Invalid response")
        elif '6' in user_msg:
            msg.body('''
            1. What are the career opportunities for the graduates of this program?\n
            2. Does VIT-AP offer Campus placement facilities?''')
            if '1' in user_msg:
                msg.body('''
                This Inter-disciplinary program brings together a lot of skills required by Data Scientists with adequate domain knowledge to help any organization find ways to take major business decisions, reduce costs, get into new markets, launch a new product or service, find the sentiment of the customers, so on. The following industries/sectors would be the expected employers.
                •	IT industries
                •	Research institutions 
                •	Banking sector
                •	Consulting firms
                •	Pharmaceutical companies
                •	Automobile industries and 
                •	Finance
                •	Educational sector
                ''')
            elif '2' in user_msg:
                msg.body(
                    "VIT Provides centralized campus placements throughout all the VIT Campuses. ")
            else:
                msg.body("Invalid response")
        else:
            msg.body("Invalid response")

    elif '0' in user_msg:
        quit()

    else:
        msg.body("Please enter the valid argument")
    return str(bot_resp)


if __name__ == '__main__':
    app.run(debug=True)
