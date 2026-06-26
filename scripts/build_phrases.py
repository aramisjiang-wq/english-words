#!/usr/bin/env python3
"""Build data/phrases.json — a scenario-organized lexical-chunk library.

Fluency is built from prefabricated chunks (collocations, fixed phrases,
sentence frames) retrieved as whole units, grouped by real-life scenario.
This is a curated *starter* library; extend SCENARIOS to grow it toward
the several-thousand chunks a fluent speaker actually uses.

Output schema mirrors words_merged.json so the app reuses the same
grid / filter / study / SRS / proficiency engine:
  theme           = 场景 (scenario)
  part_of_speech  = 类型 (短句 / 词组)
  parent_category = 短语
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "phrases.json"

# Each entry: (english, chinese, kind)  kind: "s"=短句(sentence) "c"=词组(chunk)
SCENARIOS = {
    "问候寒暄": [
        ("How's it going?", "最近怎么样？", "s"),
        ("Long time no see.", "好久不见。", "s"),
        ("What have you been up to?", "你最近在忙什么？", "s"),
        ("It's nice to finally meet you.", "很高兴终于见到你。", "s"),
        ("Take care!", "保重！", "s"),
        ("Have a good one.", "祝你愉快。", "s"),
        ("Catch you later.", "回头见。", "s"),
        ("How was your weekend?", "你周末过得怎么样？", "s"),
        ("Can't complain.", "还不错。", "s"),
        ("Same here.", "我也是。", "c"),
        ("What's new?", "有什么新鲜事吗？", "s"),
        ("Say hi to your family.", "代我向你家人问好。", "s"),
    ],
    "自我介绍": [
        ("Let me introduce myself.", "请允许我自我介绍。", "s"),
        ("I'm in charge of marketing.", "我负责市场营销。", "s"),
        ("I work as a software engineer.", "我是一名软件工程师。", "s"),
        ("I'm originally from Beijing.", "我老家在北京。", "s"),
        ("I've been here for three years.", "我在这里三年了。", "s"),
        ("a background in design", "设计相关的背景", "c"),
        ("I'm passionate about", "我热衷于……", "c"),
        ("Feel free to call me Sam.", "你可以叫我 Sam。", "s"),
        ("We met at the conference.", "我们在会议上见过。", "s"),
        ("I look forward to working with you.", "期待与你合作。", "s"),
    ],
    "餐厅点餐": [
        ("A table for two, please.", "两位，谢谢。", "s"),
        ("Could I see the menu?", "我能看下菜单吗？", "s"),
        ("What do you recommend?", "你有什么推荐？", "s"),
        ("I'll have the same.", "我要一样的。", "s"),
        ("Could I get the check, please?", "请结账。", "s"),
        ("for here or to go", "堂食还是外带", "c"),
        ("Can we split the bill?", "我们能分开付吗？", "s"),
        ("I'm allergic to nuts.", "我对坚果过敏。", "s"),
        ("Is this dish spicy?", "这道菜辣吗？", "s"),
        ("Could you make it less salty?", "能少放点盐吗？", "s"),
        ("Keep the change.", "不用找了。", "s"),
        ("a glass of water", "一杯水", "c"),
    ],
    "购物": [
        ("How much is this?", "这个多少钱？", "s"),
        ("Do you have this in a larger size?", "这个有大码的吗？", "s"),
        ("Can I try it on?", "我能试穿吗？", "s"),
        ("I'm just looking, thanks.", "我随便看看，谢谢。", "s"),
        ("Is this on sale?", "这个在打折吗？", "s"),
        ("Do you take credit cards?", "你们收信用卡吗？", "s"),
        ("Could I get a refund?", "我能退款吗？", "s"),
        ("a great deal", "很划算的交易", "c"),
        ("It doesn't fit.", "不合身。", "s"),
        ("I'll take it.", "我买了。", "s"),
        ("Can I get a receipt?", "能给我张收据吗？", "s"),
    ],
    "问路出行": [
        ("Excuse me, how do I get to the station?", "请问，去车站怎么走？", "s"),
        ("Is it within walking distance?", "走得到吗？", "s"),
        ("Go straight and turn left.", "直走然后左转。", "s"),
        ("It's just around the corner.", "就在拐角处。", "s"),
        ("How long does it take?", "要多久？", "s"),
        ("You can't miss it.", "你肯定找得到。", "s"),
        ("on your right", "在你右手边", "c"),
        ("Which line should I take?", "我该坐哪条线？", "s"),
        ("Does this bus go downtown?", "这趟车去市中心吗？", "s"),
        ("I think I'm lost.", "我好像迷路了。", "s"),
    ],
    "机场出行": [
        ("I'd like to check in.", "我想办理登机。", "s"),
        ("a window seat", "靠窗的座位", "c"),
        ("Is the flight on time?", "航班准点吗？", "s"),
        ("The flight has been delayed.", "航班延误了。", "s"),
        ("Where is the boarding gate?", "登机口在哪里？", "s"),
        ("carry-on luggage", "随身行李", "c"),
        ("I have nothing to declare.", "我没有要申报的物品。", "s"),
        ("Could you help me find my gate?", "你能帮我找登机口吗？", "s"),
        ("I missed my connection.", "我错过了转机。", "s"),
        ("baggage claim", "行李提取处", "c"),
    ],
    "酒店住宿": [
        ("I have a reservation under Li.", "我有个预订，名字是 Li。", "s"),
        ("What time is check-out?", "几点退房？", "s"),
        ("Is breakfast included?", "含早餐吗？", "s"),
        ("Could I have a wake-up call?", "能帮我设个叫醒服务吗？", "s"),
        ("The air conditioning isn't working.", "空调坏了。", "s"),
        ("a non-smoking room", "无烟房", "c"),
        ("Could you call me a taxi?", "能帮我叫辆出租车吗？", "s"),
        ("Can I leave my luggage here?", "我能把行李寄存在这吗？", "s"),
        ("checkout is at noon", "中午退房", "c"),
    ],
    "看病就医": [
        ("I'd like to make an appointment.", "我想预约。", "s"),
        ("I'm not feeling well.", "我不太舒服。", "s"),
        ("I have a sore throat.", "我嗓子疼。", "s"),
        ("It hurts right here.", "就是这里疼。", "s"),
        ("How often should I take this?", "这个我该多久吃一次？", "s"),
        ("a runny nose", "流鼻涕", "c"),
        ("I've had a headache since yesterday.", "我从昨天就头疼。", "s"),
        ("Do I need a prescription?", "我需要处方吗？", "s"),
        ("Take it twice a day.", "一天吃两次。", "s"),
    ],
    "打电话": [
        ("Could I speak to Mr. Lee, please?", "请问 Lee 先生在吗？", "s"),
        ("Who's calling, please?", "请问您是哪位？", "s"),
        ("Hold on a second.", "请稍等。", "s"),
        ("Could you take a message?", "能帮我留个口信吗？", "s"),
        ("You've got the wrong number.", "你打错电话了。", "s"),
        ("I'll call you back.", "我回头打给你。", "s"),
        ("The line is busy.", "电话占线。", "s"),
        ("Can you speak up a little?", "你能说大声点吗？", "s"),
        ("I'm calling about...", "我打来是想问……", "c"),
    ],
    "职场会议": [
        ("Let's get started.", "我们开始吧。", "s"),
        ("Let's circle back to that.", "这个我们稍后再说。", "s"),
        ("Could you walk me through it?", "你能给我讲一遍吗？", "s"),
        ("on the same page", "达成共识", "c"),
        ("Let's touch base next week.", "下周我们再沟通。", "s"),
        ("I'll keep you posted.", "我会随时通知你。", "s"),
        ("Let's take this offline.", "这个我们会后再谈。", "s"),
        ("What's the deadline?", "截止日期是什么时候？", "s"),
        ("a quick recap", "简短回顾", "c"),
        ("Does that work for you?", "这样行吗？", "s"),
        ("Let's wrap up.", "我们收尾吧。", "s"),
    ],
    "求职面试": [
        ("Tell me about yourself.", "请介绍一下你自己。", "s"),
        ("What are your strengths?", "你的优势是什么？", "s"),
        ("Why should we hire you?", "我们为什么要录用你？", "s"),
        ("I'm a quick learner.", "我学东西很快。", "s"),
        ("under pressure", "在压力之下", "c"),
        ("Where do you see yourself in five years?", "你五年后想做什么？", "s"),
        ("I have hands-on experience.", "我有实践经验。", "s"),
        ("Do you have any questions for us?", "你有什么想问我们的吗？", "s"),
        ("a team player", "有团队精神的人", "c"),
    ],
    "社交邀约": [
        ("Are you free this weekend?", "你这周末有空吗？", "s"),
        ("Do you want to grab a coffee?", "想去喝杯咖啡吗？", "s"),
        ("Let's hang out sometime.", "改天一起玩吧。", "s"),
        ("Count me in.", "算我一个。", "s"),
        ("I'd love to, but I'm busy.", "我很想去，但我有事。", "s"),
        ("Maybe some other time.", "改天吧。", "s"),
        ("It's on me.", "我请客。", "s"),
        ("What time works for you?", "你几点方便？", "s"),
        ("Let's keep in touch.", "保持联系。", "s"),
    ],
    "表达观点": [
        ("In my opinion,", "在我看来，", "c"),
        ("I see your point, but...", "我明白你的意思，但是……", "s"),
        ("That makes sense.", "有道理。", "s"),
        ("I couldn't agree more.", "我完全同意。", "s"),
        ("I'm not so sure about that.", "这点我不太确定。", "s"),
        ("It depends.", "看情况。", "s"),
        ("to be honest", "说实话", "c"),
        ("Let me put it this way.", "我换个说法。", "s"),
        ("on the other hand", "另一方面", "c"),
        ("That's a good point.", "说得好。", "s"),
    ],
    "情绪感受": [
        ("I'm thrilled about it.", "我对此很激动。", "s"),
        ("I'm a bit nervous.", "我有点紧张。", "s"),
        ("That's such a relief.", "真是松了口气。", "s"),
        ("I'm fed up with this.", "我受够了。", "s"),
        ("It drives me crazy.", "这让我抓狂。", "s"),
        ("I feel under the weather.", "我感觉不舒服。", "s"),
        ("I'm over the moon.", "我高兴极了。", "s"),
        ("It's no big deal.", "没什么大不了。", "s"),
        ("I'm in a good mood.", "我心情不错。", "s"),
    ],
    "请求帮助": [
        ("Could you give me a hand?", "你能帮我个忙吗？", "s"),
        ("Do you mind helping me?", "你介意帮我一下吗？", "s"),
        ("Could you do me a favor?", "能帮我个忙吗？", "s"),
        ("I was wondering if you could...", "不知你能否……", "c"),
        ("Let me give you a hand.", "我来帮你。", "s"),
        ("No problem at all.", "完全没问题。", "s"),
        ("Sorry to bother you.", "抱歉打扰你。", "s"),
        ("Could you explain that again?", "你能再解释一遍吗？", "s"),
        ("Thanks for your help.", "谢谢你的帮忙。", "s"),
    ],
    "道歉感谢": [
        ("I really appreciate it.", "我非常感激。", "s"),
        ("Thanks a lot for everything.", "万分感谢。", "s"),
        ("I owe you one.", "我欠你一个人情。", "s"),
        ("My apologies for the delay.", "抱歉耽搁了。", "s"),
        ("It was my fault.", "是我的错。", "s"),
        ("Don't mention it.", "别客气。", "s"),
        ("No worries.", "没关系。", "s"),
        ("I didn't mean to.", "我不是故意的。", "s"),
        ("Please forgive me.", "请原谅我。", "s"),
    ],
}

KIND_LABEL = {"s": "短句", "c": "词组"}


def build():
    out = []
    for scenario, items in SCENARIOS.items():
        for english, chinese, kind in items:
            out.append({
                "english": english.strip(),
                "phonetic": "",
                "chinese": chinese.strip(),
                "example": "",
                "category": scenario,
                "part_of_speech": KIND_LABEL[kind],
                "theme": scenario,
                "parent_category": "短语",
                "child_category": KIND_LABEL[kind],
            })
    return out


def main():
    data = build()
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {len(data)} phrases across {len(SCENARIOS)} scenarios -> {OUT.name}")
    for s, items in SCENARIOS.items():
        print(f"  {len(items):>3}  {s}")


if __name__ == "__main__":
    main()
