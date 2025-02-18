import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

const GeminiChat = () => {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const API_KEY = "YOUR_GEMINI_API_KEY";

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: "user", content: input };
    setMessages([...messages, userMessage]);
    setInput("");

    try {
      const response = await fetch("http://127.0.0.1:5000/api/gemini", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input }),
      });
      const data = await response.json();
      
      const botMessage = {
        role: "bot",
        content: data.candidates?.[0]?.content?.parts?.[0]?.text || "No response"
      };
      
      setMessages([...messages, userMessage, botMessage]);
    } catch (error) {
      console.error("Error fetching response:", error);
    }
  };

  return (
    <div className="max-w-lg mx-auto p-4">
      <Card>
        <CardContent>
          <div className="h-96 overflow-y-auto mb-4 border p-2 rounded">
            {messages.map((msg, index) => (
              <div key={index} className={`mb-2 ${msg.role === "user" ? "text-right" : "text-left"}`}>
                {/* <span className={`inline-block p-2 rounded-lg ${msg.role === "user" ? "bg-blue-500 text-white" : "bg-gray-200"}`}>
                  {msg.content}
                </span> */}
                <span className={`inline-block p-2 rounded-lg ${msg.role === "user" ? "bg-blue-500 text-white" : "bg-gray-200"}`}>
                  <ReactMarkdown remarkPlugins={[remarkGfm]}>{msg.content}</ReactMarkdown>
                </span>
              </div>
            ))}
          </div>
          <div className="flex space-x-2">
            <Input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask Gemini..."
            />
            <Button onClick={sendMessage}>Send</Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default GeminiChat;
