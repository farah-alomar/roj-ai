import { useState, useEffect, useRef } from "react";
import { api } from "../services/api";
import Message from "./Message";

export default function ChatBox() {
    const [message, setMessage] = useState("");
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);
    const [sessionId, setSessionId] = useState(null);

    const messagesEndRef = useRef(null);

    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({
            behavior: "smooth"
        });
    }, [messages, loading]);

    async function sendMessage() {
        if (!message.trim() || loading) return;

        const current = message.trim();

        setMessages(prev => [
            ...prev,
            { role: "user", text: current }
        ]);

        setMessage("");
        setLoading(true);

        try {
            const payload = {
                message: current
            };

            if (sessionId) {
                payload.session_id = sessionId;
            }

            const res = await api.post("/chat", payload);

            if (res.data.session_id) {
                setSessionId(res.data.session_id);
            }

            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    text: res.data.answer || "ما وصلني رد واضح من الخادم."
                }
            ]);
        } catch (error) {
            console.error(error);

            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    text: "حدث خطأ بالاتصال. تأكد أن الـ Backend يعمل، ثم حاول مجددًا."
                }
            ]);
        } finally {
            setLoading(false);
        }
    }

    function handleSuggestion(text) {
        setMessage(text);
    }

    return (
        <div className="flex flex-col flex-1 min-w-0 h-screen min-h-0 bg-zinc-950 text-white">
            <div className="flex-1 min-h-0 overflow-y-auto p-4 sm:p-8">
                {messages.length === 0 ? (
                    <div className="flex min-h-full flex-col items-center justify-center text-center py-8">
                        <div className="text-7xl mb-6">🤖</div>

                        <h1 className="text-4xl font-bold mb-3">
                            RojAI
                        </h1>

                        <p className="text-zinc-400 text-lg mb-10">
                            كيف يمكنني مساعدتك اليوم؟
                        </p>

                        <div className="grid grid-cols-2 gap-4 max-w-xl w-full">
                            <button
                                onClick={() => handleSuggestion("اكتب برنامج بلغة Python")}
                                className="bg-zinc-900 hover:bg-zinc-800 border border-zinc-800 rounded-xl p-5 transition"
                            >
                                💻<br />كتابة كود
                            </button>

                            <button
                                onClick={() => handleSuggestion("أخبرني عن أحدث أخبار الذكاء الاصطناعي")}
                                className="bg-zinc-900 hover:bg-zinc-800 border border-zinc-800 rounded-xl p-5 transition"
                            >
                                🌐<br />البحث على الإنترنت
                            </button>

                            <button
                                onClick={() => handleSuggestion("ساعدني في تلخيص ملف PDF")}
                                className="bg-zinc-900 hover:bg-zinc-800 border border-zinc-800 rounded-xl p-5 transition"
                            >
                                📄<br />تلخيص PDF
                            </button>

                            <button
                                onClick={() => handleSuggestion("كيف يمكنني تحليل صورة باستخدام الذكاء الاصطناعي؟")}
                                className="bg-zinc-900 hover:bg-zinc-800 border border-zinc-800 rounded-xl p-5 transition"
                            >
                                🖼️<br />تحليل صورة
                            </button>
                        </div>
                    </div>
                ) : (
                    <div className="max-w-4xl mx-auto">
                        {messages.map((msg, index) => (
                            <Message
                                key={index}
                                role={msg.role}
                                text={msg.text}
                            />
                        ))}

                        {loading && (
                            <div className="mb-4 text-left">
                                <div className="inline-block px-5 py-3 rounded-2xl bg-zinc-800 animate-pulse">
                                    🤖 RojAI يفكر...
                                </div>
                            </div>
                        )}

                        <div ref={messagesEndRef} />
                    </div>
                )}
            </div>

            <div className="shrink-0 border-t border-zinc-800 bg-zinc-950 p-4 sm:p-5">
                <form
                    onSubmit={e => {
                        e.preventDefault();
                        sendMessage();
                    }}
                    className="flex gap-3 max-w-4xl mx-auto w-full"
                >
                    <input
                        type="text"
                        value={message}
                        onChange={e => setMessage(e.target.value)}
                        placeholder="اكتب سؤالك هنا..."
                        disabled={loading}
                        className="flex-1 min-w-0 bg-zinc-900 border border-zinc-800 rounded-xl px-4 py-3 outline-none focus:border-cyan-500 transition disabled:opacity-60"
                    />

                    <button
                        type="submit"
                        disabled={!message.trim() || loading}
                        className="bg-cyan-500 hover:bg-cyan-400 text-black font-semibold px-5 sm:px-7 rounded-xl transition disabled:opacity-40 disabled:cursor-not-allowed"
                    >
                        {loading ? "..." : "إرسال"}
                    </button>
                </form>

                <p className="text-center text-xs text-zinc-500 mt-3">
                    قد يخطئ RojAI أحيانًا، فتحقّق من المعلومات المهمة.
                </p>
            </div>
        </div>
    );
}