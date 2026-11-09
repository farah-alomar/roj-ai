import { useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

export default function Message({ role, text }) {

    const isUser = role === "user";
    const [copied, setCopied] = useState(false);

    async function copyText() {

        try {

            await navigator.clipboard.writeText(text);

            setCopied(true);

            setTimeout(() => {
                setCopied(false);
            }, 1500);

        } catch (err) {

            console.error(err);

        }

    }

    return (

        <div
            className={`flex mb-5 ${
                isUser ? "justify-end" : "justify-start"
            }`}
        >

            <div
                className={`max-w-[80%] rounded-2xl shadow-md px-5 py-3 ${
                    isUser
                        ? "bg-blue-600 text-white"
                        : "bg-zinc-800 text-white"
                }`}
            >

                {!isUser && (

                    <div className="flex justify-between items-center mb-3">

                        <span className="text-xs font-semibold text-zinc-400">
                            🤖 RojAI
                        </span>

                        <button
                            onClick={copyText}
                            className="text-xs text-zinc-400 hover:text-white transition"
                        >
                            {copied ? "✅ Copied" : "📋 Copy"}
                        </button>

                    </div>

                )}

                <ReactMarkdown
                    remarkPlugins={[remarkGfm]}
                    components={{
                        code({ inline, className, children, ...props }) {

                            const match = /language-(\w+)/.exec(className || "");

                            return !inline && match ? (

                                <SyntaxHighlighter
                                    style={oneDark}
                                    language={match[1]}
                                    PreTag="div"
                                    {...props}
                                >
                                    {String(children).replace(/\n$/, "")}
                                </SyntaxHighlighter>

                            ) : (

                                <code className={className} {...props}>
                                    {children}
                                </code>

                            );

                        },
                    }}
                >
                    {text}
                </ReactMarkdown>

            </div>

        </div>

    );

}