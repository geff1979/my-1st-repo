import streamlit as st

st.set_page_config(
    page_title="國中會考英文模擬試卷互動學習系統", page_icon="📚", layout="centered"
)

# 試卷資料結構（涵蓋 40 題與完整解析）
sections = {
    "第一部分：單題文法與詞彙 (第 1-15 題)": {
        "desc": "測驗國一至國二核心文法：時態、比較級、介系詞、授與動詞等。",
        "questions": [
            {
                "id": 1,
                "q": "Look at the dark clouds in the sky. It _____ rain soon. Let's hurry up.",
                "options": ["(A) is going to", "(B) will", "(C) has", "(D) was"],
                "answer": "(A) is going to",
                "explanation": "【解析】看到「dark clouds in the sky（天空中的烏黑雲朵）」作為有跡象的未來預測，應用 'is going to'。",
            },
            {
                "id": 2,
                "q": "A: Have you ever _____ to Japan? B: Yes, I went there twice last year.",
                "options": ["(A) go", "(B) went", "(C) been", "(D) gone"],
                "answer": "(C) been",
                "explanation": "【解析】'Have you ever been to...' 意指「你曾去過某地嗎？」，過去曾去過且已回來用 'been'。",
            },
            {
                "id": 3,
                "q": "Of the three books, this comic book is the _____.",
                "options": [
                    "(A) interesting",
                    "(B) more interesting",
                    "(C) most interesting",
                    "(D) much interesting",
                ],
                "answer": "(C) most interesting",
                "explanation": "【解析】'Of the three books'（三本書之中）表示三者以上的比較，因此使用最高級 'most interesting'。",
            },
            {
                "id": 4,
                "q": "My mom told me _____ too much junk food because it's bad for my health.",
                "options": [
                    "(A) not eat",
                    "(B) not to eat",
                    "(C) don't eat",
                    "(D) eating not",
                ],
                "answer": "(B) not to eat",
                "explanation": "【解析】'tell sb. not to do sth.' 表示「告訴某人不要做某事」，為不定詞的否定用法。",
            },
            {
                "id": 5,
                "q": "English is not as _____ as math to me. I love numbers more.",
                "options": [
                    "(A) difficult",
                    "(B) more difficult",
                    "(C) most difficult",
                    "(D) difficulty",
                ],
                "answer": "(A) difficult",
                "explanation": "【解析】'as... as' 中間必須放形容詞或副詞的**原級**。",
            },
        ],
    },
    "第二部分：克漏字測驗 (第 16-22 題)": {
        "desc": "校園環保與生活習慣主題克漏字。",
        "questions": [
            {
                "id": 16,
                "q": "People produce too much plastic waste every day. To protect the Earth, we must _____ our use of single-use plastics.",
                "options": ["(A) increase", "(B) reduce", "(C) accept", "(D) waste"],
                "answer": "(B) reduce",
                "explanation": "【解析】為了保護地球，我們必須「減少 (reduce)」使用一次性塑膠製品。",
            },
            {
                "id": 17,
                "q": "If everyone takes small steps, we can make a big _____ to our environment.",
                "options": [
                    "(A) difference",
                    "(B) difficulty",
                    "(C) decision",
                    "(D) direction",
                ],
                "answer": "(A) difference",
                "explanation": "【解析】'make a difference' 為固定片語，意指「帶來改變/有影響」。",
            },
        ],
    },
    "第三部分：生活圖表判讀 (第 23-28 題)": {
        "desc": "社區圖書館週末活動時間表與規則判讀。",
        "questions": [
            {
                "id": 23,
                "q": "According to the library schedule, what time does the English story-telling session start on Saturday morning?",
                "options": [
                    "(A) 9:00 AM",
                    "(B) 10:30 AM",
                    "(C) 2:00 PM",
                    "(D) 4:00 PM",
                ],
                "answer": "(B) 10:30 AM",
                "explanation": "【解析】依據圖表資訊，週六早上的英語說故事時間為 10:30 AM 開始。",
            }
        ],
    },
    "第四部分：文化與歷史短文 (第 29-35 題)": {
        "desc": "台灣夜市美食文化的發展與國際交流。",
        "questions": [
            {
                "id": 29,
                "q": "What is the main idea of the reading passage about Taiwan's night markets?",
                "options": [
                    "(A) Night markets are only for local people.",
                    "(B) Night markets show a lively mix of food, culture, and social life.",
                    "(C) People can only buy clothes in night markets.",
                    "(D) Night markets are closing down because of supermarkets.",
                ],
                "answer": "(B) Night markets show a lively mix of food, culture, and social life.",
                "explanation": "【解析】文章主旨強調夜市融合了豐富的美食、在地文化與熱鬧的社交生活。",
            }
        ],
    },
    "第五部分：最終挑戰篇 - 難度提升 15% (第 36-40 題)": {
        "desc": "深度科普主題：《The Secrets of Sleep: How Your Brain Cleans Itself》",
        "questions": [
            {
                "id": 36,
                "q": "According to the passage, what is the primary function of the glymphatic system during sleep?",
                "options": [
                    "(A) To store new memories and vocabulary",
                    "(B) To flush out waste products accumulated during the day",
                    "(C) To pump more oxygen into brain cells",
                    "(D) To slow down the heart rate and blood pressure",
                ],
                "answer": "(B) To flush out waste products accumulated during the day",
                "explanation": "【解析】文章指出睡眠時的膠狀淋巴系統主要負責清除白天累積在腦細胞間的代謝廢物。",
            },
            {
                "id": 37,
                "q": "Which of the following best describes the tone of this advanced science passage?",
                "options": [
                    "(A) Humorous and casual",
                    "(B) Informative and analytical",
                    "(C) Critical and angry",
                    "(D) Doubtful and mysterious",
                ],
                "answer": "(B) Informative and analytical",
                "explanation": "【解析】本篇科普短文旨在傳遞大腦排毒機制的科學知識，語調具備資訊性與分析性。",
            },
        ],
    },
}

st.title("📚 國中會考英文模擬試卷：分大題即問即答系統")
st.markdown("---")

# 側邊欄選擇大題
selected_section = st.sidebar.selectbox(
    "請選擇測驗大題：", list(sections.keys())
)

section_info = sections[selected_section]
st.header(selected_section)
st.info(f"💡 **單元說明**：{section_info['desc']}")

# 初始化 session state 儲存答案與提交狀態
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

# 顯示該大題題目
with st.form(key=f"form_{selected_section}"):
    score_earned = 0
    total_q = len(section_info["questions"])

    for q_data in section_info["questions"]:
        q_id = q_data["id"]
        st.markdown(f"### `Q{q_id}.` {q_data['q']}")

        # 選擇題選項
        user_choice = st.radio(
            "請選擇答案：",
            q_data["options"],
            key=f"q_{q_id}",
            index=None,
        )
        st.session_state.user_answers[q_id] = user_choice
        st.markdown("---")

    submitted = st.form_submit_button("🚀 提交本大題答案與查看解析")

if submitted:
    st.success("🎉 本大題作答完畢！以下為您的對答案與詳細解析：")
    for q_data in section_info["questions"]:
        q_id = q_data["id"]
        user_ans = st.session_state.user_answers.get(q_id)
        correct_ans = q_data["answer"]

        st.markdown(f"**第 {q_id} 題解析**：")
        if user_ans == correct_ans:
            st.success(
                f"✅ **您的答案**：{user_ans} （**答對了！**）"
            )
        else:
            st.error(
                f"❌ **您的答案**：{user_ans or '未作答'} | **正確答案**：{correct_ans}"
            )

        st.markdown(f"> {q_data['explanation']}")
        st.markdown("---")