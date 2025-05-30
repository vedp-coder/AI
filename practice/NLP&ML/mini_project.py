import pandas as pd

data = {

    "emails" : [
    "Your password has expired. Click here to reset.",
    "Meeting agenda for tomorrow's standup.",
    "We detected unusual activity in your bank account.",
    "Lunch at the new cafe this Friday?",
    "You’ve been selected to win a new iPhone!",
    "Let’s finalize the project by end of this week.",
    "Verify your identity to avoid account suspension.",
    "Reminder: doctor's appointment at 3pm.",
    "Your package is waiting. Pay the customs fee now.",
    "Can you review the slides for Monday’s presentation?",

    "This is your last chance to claim your prize!",
    "Please find attached your pay slip.",
    "Update your billing information immediately.",
    "Join us for a quick sync at 2pm?",
    "Claim your free vacation now!",
    "Your Zoom link for today’s meeting is below.",
    "Unusual sign-in attempt detected. Act now!",
    "What time should we meet at the library?",
    "Confirm your details to avoid legal action.",
    "Team dinner at 6:30 today, don’t forget!",

    "Reactivate your suspended account immediately.",
    "Thank you for your recent purchase.",
    "PayPal alert: Suspicious login detected.",
    "Project kickoff call scheduled at 10am.",
    "You’ve been hacked. Change your password.",
    "Reminder: Book club meets tonight!",
    "Click here to unlock your frozen funds.",
    "Are you joining the game night later?",
    "Warning: Security breach. Urgent action required.",
    "Let’s grab coffee this afternoon!",

    "Final notice: Your credit card is at risk.",
    "See you at the gym at 5?",
    "Email verification needed to keep your account active.",
    "Awesome job on the presentation today!",
    "Click to receive your $100 Amazon gift card.",
    "Dinner reservations confirmed for 7pm.",
    "Immediate action required: tax documents pending.",
    "What’s your availability for the team check-in?",
    "Urgent alert from your email provider.",
    "Let’s finalize the group project tonight.",

    "Update your security questions to keep your account safe.",
    "Team huddle rescheduled to 11am.",
    "Act now to claim your digital currency bonus.",
    "Meeting link for tomorrow’s workshop.",
    "Alert: login attempt from unknown device.",
    "Wanna go hiking this weekend?",
    "Resolve payment failure now to avoid penalty.",
    "Happy birthday! Hope it’s a great one.",
    "Your account is on hold. Reactivate now.",
    "Final edits on the report look great!"
],

"labels" : [
    "phishing", "legit", "phishing", "legit", "phishing",
    "legit", "phishing", "legit", "phishing", "legit",

    "phishing", "legit", "phishing", "legit", "phishing",
    "legit", "phishing", "legit", "phishing", "legit",

    "phishing", "legit", "phishing", "legit", "phishing",
    "legit", "phishing", "legit", "phishing", "legit",

    "phishing", "legit", "phishing", "legit", "phishing",
    "legit", "phishing", "legit", "phishing", "legit",

    "phishing", "legit", "phishing", "legit", "phishing",
    "legit", "phishing", "legit", "phishing", "legit"
]
}

ff = pd.DataFrame(data)
print(ff)

from sklearn.feature_extraction.text import TfidfVectorizer
vect = TfidfVectorizer()
vects = vect.fit_transform(ff["emails"])
print("TF-IDF Matrix shape:", vects.shape)
print("Words used (features):", vect.get_feature_names_out()) # Change vects to vect

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X_train, X_test, Y_train, Y_test = train_test_split(vects, ff["labels"], test_size=0.3, random_state=42)

# Create the robot brain (model)
model = LogisticRegression()

# Teach the robot using the training data
model.fit(X_train, Y_train)

from sklearn.metrics import accuracy_score, classification_report

# Step 1: Use the model to predict on the test set
y_pred = model.predict(X_test)

# Step 2: Compare predictions with actual answers
print("Accuracy:", accuracy_score(Y_test, y_pred))

# Step 3: See detailed results
print("\nClassification Report:\n", classification_report(Y_test, y_pred))

new_emails = input("Paste an email here: ")
new_emails_vect = vect.transform([new_emails])
predictions = model.predict(new_emails_vect)
print("Prediction:", predictions)
