# 🚀 AI Scrum Assistant - with Predictive Analytics

An intelligent Sprint management tool powered by Streamlit and OpenAI's GPT models to provide AI-driven insights and predictive analytics for your agile teams.

## Features

✅ **Sprint Data Management**
- Upload and view sprint data from CSV files
- Real-time metrics and status tracking
- Blocked items identification

✅ **Sprint Analytics**
- Completion rates and velocity tracking
- Risk assessment and trend analysis
- Status distribution visualization

✅ **AI-Powered Insights** (NEW!)
- Sprint health assessment
- Automated risk detection
- Root cause analysis
- Predictive recommendations
- Powered by OpenAI GPT-4o-mini

## Setup Instructions

### 1. Install Dependencies
```bash
pip install streamlit pandas openai
```

### 2. Get an OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/account/api-keys)
2. Sign up or log in to your account
3. Click "Create new secret key"
4. Copy your API key (starts with `sk-`)

### 3. Configure Your API Key

**Option A: Sidebar Input (Recommended)**
- Run the app: `streamlit run app.py`
- Paste your API key in the "⚙️ Configuration" panel on the left
- The key is stored in your session only (not saved)

**Option B: Environment Variable (For Local Development)**
1. Create/edit `.env` file in the project directory:
   ```
   OPENAI_API_KEY=sk-your-api-key-here
   ```
2. Install python-dotenv: `pip install python-dotenv`
3. The app will automatically load it

### 4. Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8502`

## How to Use

### Tab 1: 📊 All Data
- View your complete sprint data in a table
- See all sprints, stories, and statuses

### Tab 2: 📈 Sprint Summary
- View completion percentage for each sprint
- Detailed breakdown of Done/In Progress/To Do items
- Expand each sprint to see detailed metrics

### Tab 3: 🎯 Metrics
- Overall statistics (total story points, completion rate, etc.)
- Status distribution chart
- View all blocked items

### Tab 4: 🧠 AI Insights
- Click "🚀 Generate AI Insights" to analyze your sprint
- Get automated analysis including:
  - **Sprint Health Assessment** - Overall status and trajectory
  - **Key Risks** - Top risks that could impact delivery
  - **Root Cause Analysis** - Why these risks exist
  - **Predictive Insights** - Future trends if current status continues
  - **Recommendations** - Actionable steps to improve

## CSV File Format

Your `sprint_data.csv` should have these columns:
```
Sprint,Story,Status,StoryPoints,Blocked
Sprint 1,Login API,Done,5,No
Sprint 1,Payment API,Done,8,No
```

Required columns:
- **Sprint**: Sprint identifier (e.g., "Sprint 1")
- **Story**: Story/Task name
- **Status**: One of "Done", "In Progress", "To Do"
- **StoryPoints**: Numeric value (1, 2, 3, 5, 8, etc.)
- **Blocked**: "Yes" or "No"

## Security Notes

⚠️ **Never commit your API key to GitHub!**
- The `.gitignore` file protects `.env` files
- Use the sidebar input for API keys (not saved to disk)
- Create a separate API key for testing if needed

## Cost Information

OpenAI API usage is charged based on tokens consumed.
- **GPT-4o-mini**: ~$0.15 per 1M input tokens, $0.60 per 1M output tokens
- Average sprint analysis: 5-10 cents per request
- **Free option**: Use sidebar to test without real API key

## Troubleshooting

### "API Key not found" error
- Make sure you've entered the key in the sidebar
- Or set the `OPENAI_API_KEY` environment variable
- Restart the Streamlit app

### "CSV file not found" error
- Ensure `sprint_data.csv` is in the same directory as `app.py`
- Check the file path is correct

### API rate limit error
- Wait a few minutes before trying again
- Check your OpenAI account usage at https://platform.openai.com/account/billing/limits

## File Structure

```
AI_Scrum_Assistant/
├── app.py                  # Main Streamlit application
├── sprint_data.csv         # Your sprint data (can be updated anytime)
├── .env                    # API key configuration (not in Git)
├── .gitignore              # Git ignore rules
├── README.md               # This file
└── .git/                   # Git repository
```

## Next Steps

1. ✅ Install requirements:
   ```bash
   pip install streamlit pandas openai
   ```

2. ✅ Get your OpenAI API key from https://platform.openai.com/account/api-keys

3. ✅ Run the app:
   ```bash
   streamlit run app.py
   ```

4. ✅ Enter your API key in the sidebar "⚙️ Configuration"

5. ✅ Navigate to "🧠 AI Insights" tab and click "Generate AI Insights"

## Support

For issues or questions:
- Streamlit docs: https://docs.streamlit.io
- OpenAI docs: https://platform.openai.com/docs
- GitHub issues: Create an issue in your repository

Enjoy your AI-powered Sprint Assistant! 🚀
