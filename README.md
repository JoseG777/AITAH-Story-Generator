# r/AITAH Story Generator
## About:
This project helps users who can't get enough of the latest trending stories from the r/AITAH subreddit by creating new, unique stories. Utilizing Tavily's API, the program fetches the most trending r/AITAH stories and employs OpenAI to generate new stories based on the fetched information.


## How It Works
The program consists of three agents:
1. **Search Agent**: Uses Tavily's API to search for trending r/AITAH stories.
2. **Creation Agent**: Takes the fetched content and employs OpenAI to create a unique story based on the information.
3. **Validation Agent**: Ensures the coherence and quality of the generated story, asking OpenAI to revise if necessary.


## How to use:
1. Set up virtual environment:
```bash
python3 -m venv venv
```

2. Activate virtual environment:
For Linux:
```bash
source venv/bin/activate
```
For Windows:
```bash
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
OPENAI_API_KEY="your_openai_api_key"

TAVILY_API_KEY="your_tavily_api_key"
```

5. Run the program:
```bash
python3 main.py
```

To get a free Tavily API key, visit [Tavily](https://tavily.com/)

## Example outputs:
```bash
Story with 10 inputs:
I (28F) and my boyfriend (30M), let's call him Dave, have been together for three years. We recently moved into a new apartment together, and things have been mostly great, except for one issue that's been driving me insane.

Dave has a habit of ordering food delivery almost every single day. It's not like we can't cook; we have a fully stocked kitchen, and I enjoy cooking. But Dave prefers the convenience of delivery. He always justifies it by saying he's too tired from work, and while I understand that, it’s starting to affect our budget.

A few weeks ago, I decided to talk to him about it. I suggested that we cook at home more often to save money and maybe use the extra cash for a nice vacation or something. Dave agreed, but his actions didn't change. He kept ordering food, sometimes even twice a day.

Last week, I hit my breaking point. We had a small argument about finances, and I brought up his excessive spending on food deliveries. Dave got defensive and said I was overreacting. In a moment of frustration, I canceled his food delivery account without telling him. I figured it would force him to cut back at least for a while.

When Dave tried to order lunch the next day and found out his account was canceled, he was furious. He accused me of being controlling and disrespectful. I told him I did it because he wasn't taking our financial situation seriously, but he said that wasn't my decision to make.

Now, we're barely speaking, and I'm starting to wonder if I went too far. AITAH for canceling my boyfriend's food delivery account without his permission?
```

```bash
Story with 5 inputs:
Title: AITAH for Refusing to Wear Traditional Attire to My Friend's South Asian Wedding?

Hey everyone,

I (29F) need some perspective on a situation that happened recently. My best friend, Priya (28F), invited me to her wedding, which was a grand South Asian celebration. We've been friends since college, and I was thrilled to be part of her big day.

Prior to the wedding, Priya gave all her bridesmaids (myself included) traditional outfits to wear. The outfits were beautiful, but they were extremely heavy and ornate. I have a medical condition that makes it difficult for me to wear heavy clothing for extended periods of time. I explained this to Priya, thinking she would understand.

To my surprise, Priya was very upset. She insisted that the traditional outfits were essential for the wedding’s aesthetic and cultural significance. I proposed wearing a lighter, simpler version of the traditional attire, but still in the same color scheme. Priya was not happy with this compromise and said I would be ruining the photos and the whole ambiance of the wedding.

On the day of the wedding, I showed up in the lighter version of the outfit. Priya was visibly upset but didn't say anything to me during the event. Later, she sent me a long text expressing her disappointment and accusing me of being disrespectful to her culture and her big day. She said that all the other bridesmaids managed to wear the traditional attire without complaints.

I feel terrible because I never intended to disrespect Priya or her culture. I just wanted to be comfortable and avoid any health issues. Some of our mutual friends think I should have just sucked it up for one day, while others believe Priya was being unreasonable.

So, AITAH for not wearing the traditional attire to my friend’s wedding?

Looking forward to hearing your thoughts.
```
