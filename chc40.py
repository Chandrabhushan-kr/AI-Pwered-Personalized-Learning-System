import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        st.error("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        st.error("Could not request results; {0}".format(e))
        return ""

def suggest_books(subject, marks, class_level):
    # book recommendations 
    book_recommendations = {
        1: {
            'Math': {'Basic': ['Book 1', 'Book 2'], 'Advanced': ['Book 3', 'Book 4']},
            'Physics': {'Basic': ['Book 5', 'Book 6'], 'Advanced': ['Book 7', 'Book 8']},
            'Chemistry': {'Basic': ['Book 9', 'Book 10'], 'Advanced': ['Book 11', 'Book 12']},
            'Biology': {'Basic': ['Book 13', 'Book 14'], 'Advanced': ['Book 15', 'Book 16']},
            'English': {'Basic': ['Book 17', 'Book 18'], 'Advanced': ['Book 19', 'Book 20']}
        },
        2: {
            # Add book recommendations for class 2 here
            'Math': {'Basic': ['Book 21', 'Book 22'], 'Advanced': ['Book 23', 'Book 24']},
            'Physics': {'Basic': ['Book 25', 'Book 26'], 'Advanced': ['Book 27', 'Book 28']},
            'Chemistry': {'Basic': ['Book 29', 'Book 30'], 'Advanced': ['Book 31', 'Book 32']},
            'Biology': {'Basic': ['Book 33', 'Book 34'], 'Advanced': ['Book 35', 'Book 36']},
            'English': {'Basic': ['Book 37', 'Book 38'], 'Advanced': ['Book 39', 'Book 40']}
        },
        # Add book recommendations for other class levels here
    }

    # Determine level of books based on marks
    if marks < 50:
        level = 'Basic'
    else:
        level = 'Advanced'

    # Retrieve book recommendations for the selected subject, marks, and class level
    recommendations = book_recommendations.get(class_level, {}).get(subject, {}).get(level, [])

    return recommendations

def academic_helper():
    st.write("Hello Dear, Welcome to the best and your only education assistance app.")
    st.title("Your Academic Helper")
    st.markdown("Give us your basic details")

    name = st.text_input('What Is Your Name')

    College = st.radio('Pick Your Dream', ['IIT', 'NIT'])

    if College == 'IIT':
        Category = st.radio('Category', ['OPEN', 'EWS', 'OBC-NCL', 'ST', 'SC'])
        Program = st.selectbox('Pick a program', [
            " Bachelor of Technology",
            " Bachelor and Master of Technology ",
            " Bachelor of Science",
            " Bachelor of Architecture",
            " Bachelor of Science and Master of Science ",
            " Integrated Master of Technology"
        ])
        Branch = st.selectbox("Interests/Preferences: ", ["Civil Engineering ", "Civil Engineering and M. Tech. in Structural Engineering ", "Civil Engineering and M.Tech in Transportation Engineering ", "Civil Engineering and M.Tech. in Environmental Engineering ", "Computer Science and Engineering ", "Electrical Engineering and M.Tech Power Electronics and Drives ", "Electrical Engineering ", "Electronics and Communication Engineering ", "Mechanical Engineering ", "Mechanical Engineering and M. Tech. in Mechanical System Design ", "Mechanical Engineering and M. Tech. in Thermal Science & Engineering ", "Mechanical Engineering with M.Tech. in Manufacturing Engineering ", "Metallurgical and Materials Engineering ", "Aerospace Engineering ", "BS in Mathematics ", "Chemical Engineering ", "Chemistry ", "Economics ", "Energy Engineering ", "Engineering Physics ", "Environmental Science and Engineering ", "Mechanical Engineering and M.Tech. in Computer Integrated Manufacturing ", "Metallurgical Engineering and Materials Science ", "Bio Engineering ", "Data Science and Engineering ", "Biotechnology and Biochemical Engineering ", "Engineering and Computational Mechanics ", "Materials Engineering ", "Mathematics and Computing ", "Production and Industrial Engineering ", "Textile Technology ", "Agricultural and Food Engineering ", "Agricultural and Food Engineering with M.Tech. in any of the listed specializations ", "Applied Geology ", "Architecture ", "Civil Engineering with any of the listed specialization ", "Electrical Engineering with M.Tech. in any of the listed specializations ", "Electronics and Electrical Communication Engineering ", "Electronics and Electrical Communication Engineering with M.Tech. in any of the listed specializations ", "Exploration Geophysics ", "Industrial and Systems Engineering ", "Industrial and Systems Engineering with M.Tech. in Industrial and Systems Engineering and Management ", "Instrumentation Engineering ",
                              "Manufacturing Science and Engineering ", "Manufacturing Science and Engineering with M.Tech. in Industrial and Systems Engineering and Management ", "Mechanical Engineering with M.Tech. in any of the listed specializations ", "Mining Engineering ", "Mining Safety Engineering ", "Ocean Engineering and Naval Architecture ", "Physics ", "Artificial Intelligence ", "Biomedical Engineering ", "Biotechnology and Bioinformatics ", "Computational Engineering ", "Engineering Science ", "Industrial Chemistry ", "Materials Science and Metallurgical Engineering ", "Artificial Intelligence and Data Science ", "Chemistry with Specialization ", "Civil and Infrastructure Engineering ", "Physics with Specialization ", "Biological Sciences and Bioengineering ", "Earth Sciences ", "Materials Science and Engineering ", "Mathematics and Scientific Computing ", "Statistics and Data Science ", "Biological Engineering ", "Biological Sciences ", "Engineering Design ", "Naval Architecture and Ocean Engineering ", "Electrical and Electronics Engineering ", "Biosciences and Bioengineering ", "Chemical Sciences ", "Data Science and Artificial Intelligence ", "Geological Technology ", "Geophysical Technology ", "Mathematics & Computing ", "Applied Geophysics ", "Environmental Engineering ", "Mineral and Metallurgical Engineering ", "Mining Machinery Engineering ", "Petroleum Engineering ", "Biochemical Engineering with M.Tech. in Biochemical Engineering and Biotechnology ", "Bioengineering with M.Tech in Biomedical Technology ", "Ceramic Engineering ", "Electrical Engineering with M.Tech. in Power Electronics ", "Electronics Engineering ", "Materials Science and Technology ", "Metallurgical Engineering ", "Pharmaceutical Engineering & Technology ", "Chemical Science and Technology ", "Electronics and Electrical Engineering ", "Mechatronics Engineering ", "Chemical and Biochemical Engineering ", "Interdisciplinary Sciences "])

        Rank = st.number_input('JEE Advance Rank', 1)

        data = pd.read_excel('Copy of IITJEE(1).xlsx', usecols=[
            'NIRF','Institute', 'Academic Program Name', 'Course', 'Seat Type', 'Opening Rank', 'Closing Rank'])


        # Display the filtered data

        df = pd.DataFrame(data)

        df['Opening Rank'] = pd.to_numeric(df['Opening Rank'], errors='coerce')
        df['Closing Rank'] = pd.to_numeric(df['Closing Rank'], errors='coerce')

        df = df[(df['Opening Rank'] >= Rank) & (df['Closing Rank'] <= Rank + 10000) &
                (df['Seat Type'] == Category) & (df['Course'] == Program) & (df['Academic Program Name'] == Branch)]

        df.sort_values(by='Opening Rank', inplace=True)
        df = df.reset_index(drop=True)
        st.dataframe(df)

    else:
        Category = st.radio('Category', ['OPEN', 'EWS', 'OBC-NCL', 'ST', 'SC'], key='category_radio')
        CState = st.select_slider('College State', ['Home', 'Other', 'Any'], key='state_slider')
        if CState == "Home":
            CState = "HS"
        elif CState == "Other":
            CState = "OS"
        else:
            CState = ''
        Program = st.selectbox('Pick a program', [
            " Bachelor of Technology",
            " Bachelor of Architecture",
            " Bachelor and Master of Technology ",
            " Bachelor of Planning",
            " Bachelor of Science and Master of Science ",
            " Integrated Master of Science"
        ])
        Branch = st.selectbox("Interests/Preferences: ", ["Electronics and Communication Engineering ", "Bio Technology ", "Chemical Engineering ", "Civil Engineering ", "Computer Science and Engineering ", "Electrical Engineering ", "Industrial and Production Engineering ", "Information Technology ", "Instrumentation and Control Engineering ", "Mechanical Engineering ", "Textile Technology ", "Architecture ", "Metallurgical and Materials Engineering ", "Materials Science and Metallurgical Engineering ", "Mathematics and Data Science ", "Planning ", "Production and Industrial Engineering ", "Biotechnology and Biochemical Engineering ", "Chemistry ", "Computational Mathematics ", "Electronics and Instrumentation Engineering ", "Engineering Physics ", "Mathematics & Computing ", "Physics ", "Production Engineering ", "Electrical and Electronics Engineering ", "Materials Science and Engineering ", "Biotechnology ", "Mathematics and Computing ", "Artificial Intelligence ", "Computational and Data Science ",
                              "Mining Engineering ", "Civil Engineering with Specialization in Construction Technology and Management ", "Computer Science and Engineering with Specialization in Cyber Security ", "Computer Science and Engineering with Specialization in Data Science ", "Electrical Engineering with Specialization In Power System Engineering ", "Electronics and Communication Engineering with Specialization in Microelectronics and VLSI System Design ", "Material Science and Engineering ", "Mathematics and Computing Technology ", "Mechanical Engineering with Specialization in Manufacturing and Industrial Engineering ", "Bio Medical Engineering ", "Engineering and Computational Mechanics ", "Computer Engineering ", "Ceramic Engineering ", "Ceramic Engineering and M.Tech Industrial Ceramic ", "Food Process Engineering ", "Industrial Design ", "Life Science ", "Mathematics ", "Aerospace Engineering ", "Electronics and Telecommunication Engineering ", "Metallurgy and Materials Engineering "])

        Rank = st.number_input('JEE Mains Rank', 1)

        data = pd.read_excel('Copy of JEE(1).xlsx', usecols=[
            'NIRF','Institute', 'Academic Program Name', 'Course', 'Quota', 'Seat Type', 'Opening Rank', 'Closing Rank'])
        df = pd.DataFrame(data)
        if CState == '':
            df = df.query('`Opening Rank` >= {} and `Closing Rank` <= {} and `Seat Type` == "{}" and `Course` == "{}" and `Academic Program Name` == "{}"'.format(
                Rank, Rank+10000, Category, Program, Branch))
        else:
            df = df.query('`Opening Rank` >= {} and `Closing Rank` <= {} and Quota == "{}" and `Seat Type` == "{}" and `Course` == "{}" and `Academic Program Name` == "{}"'.format(
                Rank, Rank+10000, CState, Category, Program, Branch))
        df.sort_values(by='Opening Rank', inplace=True)
        # table = st.table(df)
        df = df.reset_index(drop=True)
        st.dataframe(df)

    bid = pd.read_excel('Book1 .xlsx', usecols=['Academic Program Name', 'Books', 'Book Author', 'Purchasing Link', 'Courses', 'Platform', 'Course Link'])

    # Filter the DataFrame based on the selected branch
    filtered_data = bid[bid['Academic Program Name'] == Branch]
    book_df = filtered_data[['Books', 'Book Author', 'Purchasing Link']]

    # Create a DataFrame for course-related information
    course_df = filtered_data[['Courses', 'Platform', 'Course Link']]
    book_df = book_df.reset_index(drop=True)
    course_df = course_df.reset_index(drop=True)
    st.markdown("Hi, " + name + "! Based On Your Interest , We Have Some Book Recommendation")
    st.dataframe(book_df)

    st.markdown("Hi Again 😎, " + name + " ! Based On Your Interest , We Have Some Online Course Recommendation")

    st.dataframe(course_df)

    st.title("Subject Marks Entry and Book Recommendations")

    # Create a DataFrame to store student's name, class, subject, marks, and answers
    data = {
        'Name': [],
        'Class': [],
        'Subject': [],
        'Marks': [],
        'Answer': [],
        'Score': [],
        'Book Recommendation': []  # Add column for book recommendation
    }

    # Collecting class information
    class_level = st.select_slider("Select Class (1-10)", options=list(range(1, 11)))

    total_marks = 0
    total_score = 0
    correct_answers = 0
    wrong_answers = 0

    # Collecting marks, asking questions, and calculating score for each subject
    subject_options = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
    for subject in subject_options:
        marks = st.number_input(f"Enter {subject} Marks", min_value=0, max_value=100, step=1, key=f"{subject}_marks")
        total_marks += marks

        # Ask a question based on the marks
        if marks < 50:
            question = f"What is the formula of (a+b)2?"
            correct_answer = "a2+b2+2ab"
        else:
            question = f"What formula of (a + b)3?"
            correct_answer = "a3+b3+3ab(a+b)"
        
        # Display MCQ question for Physics and Chemistry subjects
        if subject in ['Physics', 'Chemistry']:
            st.write(f"Question for {subject} (MCQ):", question)
            # Options for MCQ
            options = ['a2+b2+2ab', 'a2-b2', 'a3+b3', 'ab+ba']
            # Append a unique identifier to the key argument
            radio_key = f"{subject}_radio"
            selected_option = st.radio("Select the correct option:", options,key=radio_key)
            if selected_option == correct_answer:
                st.success("Correct!")
                score = 1
                correct_answers += 1
            else:
                st.error("Wrong! The correct answer is:", correct_answer)
                score = 0
                wrong_answers += 1
        else:
            answer = st.text_input(question, key=f"{subject}_question")

            # Compare the user's answer with the correct answer
            if answer.lower() == correct_answer.lower():
                st.success("Correct!")
                score = 1
                correct_answers += 1
            else:
                # st.error(f"Wrong! The correct answer is '{correct_answer}'.")
                score = 0
                wrong_answers += 1

        total_score += score

        # Get book recommendation based on subject, marks, and class level
        book_recommendation = suggest_books(subject, marks, class_level)

        # Append the collected data to the DataFrame
        data['Name'].append(name)
        data['Class'].append(class_level)
        data['Subject'].append(subject)
        data['Marks'].append(marks)
        data['Answer'].append(answer)
        data['Score'].append(score)
        data['Book Recommendation'].append(book_recommendation)  # Add book recommendation to data

    # Create a DataFrame from the collected data
    df = pd.DataFrame(data)

    # Display the DataFrame
    st.write("Entered Marks, Answers, and Scores:")
    st.write(df)

    # Display total score, total marks, and number of correct and wrong answers
    st.write(f"Total Score: {total_score}")
    st.write(f"Total Marks: {total_marks}")
    st.write(f"Number of Correct Answers: {correct_answers}")
    st.write(f"Number of Wrong Answers: {wrong_answers}")

    # Plotting graphs
    st.title("Graphs")
    st.write("Here are some visualization of your academic performance:")

    # 1. Bar plot
    st.subheader("1. Bar Plot")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Subject', y='Marks', data=df)
    plt.title("Marks Distribution by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    st.pyplot()

    # 2. Pie chart
    st.subheader("2. Pie Chart")
    plt.figure(figsize=(8, 8))
    df['Score'].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title("Score Distribution")
    st.pyplot()

    # 3. Line plot
    st.subheader("3. Line Plot")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='Subject', y='Marks', marker='o')
    plt.title("Marks Trend by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    st.pyplot()

    # 4. Scatter plot
    st.subheader("4. Scatter Plot")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Marks', y='Score', hue='Subject')
    plt.title("Marks vs. Score")
    plt.xlabel("Marks")
    plt.ylabel("Score")
    st.pyplot()

    st.set_option('deprecation.showPyplotGlobalUse', False)

def home():
    st.title("Home Page")
    st.header("Welcome to Personalized Learning System")
    st.subheader("Understand the learning preferences, strengths, and weaknesses of each student.It will provide personalized learning materials based on the learning preferences and level of understanding of the student.")
    st.text("Choose a Service from the left sidebar.")

def voice_chat():
    st.title("Voice Chat")
    st.write("Click the button below and speak into your microphone:")
    if st.button("Start Recording"):
        text = recognize_speech()
        st.write("You said:", text)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Academic Helper", "Voice Chat"])

# Display the selected page
if page == "Home":
    home()
elif page == "Academic Helper":
    academic_helper()
elif page == "Voice Chat":
    voice_chat()
