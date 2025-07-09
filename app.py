from flask import Flask, render_template

app = Flask(__name__)

BOOKS= [
    {
        'title': "Can't Hurt Me: Master Your Mind and Defy the Odds",
        'author': 'David Goggins',
        'description': "A powerful memoir and guide to mental toughness. David Goggins shares his story of overcoming childhood abuse, obesity, and failure to become a Navy SEAL and elite athlete, teaching how to push past limits.",
        'image': 'static/cant_hurt_me.jpg'
    },
    {
        'title': "The Boron Letters",
        'author': 'Gary C. Halbert',
        'description': "A series of letters from legendary copywriter Gary Halbert to his son. This book blends timeless lessons on direct marketing with life advice, making it a classic for entrepreneurs and marketers.",
        'image': 'static/boron_letters.jpg'
    },
    {
        'title': "Start With Why: How Great Leaders Inspire Everyone to Take Action",
        'author': 'Simon Sinek',
        'description': "Simon Sinek explores how great leaders inspire action by starting with a clear sense of purpose—their 'Why.' The book introduces the Golden Circle model: Why, How, What.",
        'image': 'static/start_with_why.jpeg'
    }
]


@app.route('/')
def hello_world():
  return render_template('blog.html',books=BOOKS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
