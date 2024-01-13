# AnyCheck: Intelligent Fact Verification

AnyCheck Fact Checker is an innovative web application designed to enhance the accuracy of information dissemination. This project is currently being expanded to support fact-checking and suggestions for real-time conversations, including meetings, presentations, debates, etc. 

Leveraging a pre-trained large language model with additional custom training, AnyCheck provides users with a reliable platform to verify the authenticity of their claims and essays. The application features a user-friendly interface with voice-enabled functionalities, allowing users to speak their claims or upload essays for review simply. With AnyCheck, users can expect a seamless fact-checking experience, complete with detailed analysis and accuracy percentages, fostering a more informed and truthful online environment.

Key Features:
- Voice-Activated Claims Submission: Initiate fact-checking by speaking your claim, thanks to integrated speech recognition.
- PDF Essay Analysis: Upload your essays in PDF format for a comprehensive factual accuracy review.
- Real-Time Feedback: Receive immediate alerts classifying claims or essays as true, partially false, or false with specific breakdowns and an accuracy percentage. 
- Trained Language Model: Benefit from a bespoke language model tailored to provide precise fact-checking results.

Whether you're a student, educator, journalist, or just someone keen on verifying information, AnyCheck Fact Checker is your go-to tool for ensuring the integrity of your content.

Verify the accuracy of your essay using a pre-trained large language model, enhanced with additional training and customizations. 

# Running the application:

Run the following command in the terminal:

```
  flask run
```

This will get the project running locally on your machine. You can open the link that "flask run" provides to open the link locally on your machine.

# Running the Frontend:

To get tailwind installed, run

```sh
npm install
```

Then, to make sure the generated css remains up to date as you are working, run

```sh
npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
```