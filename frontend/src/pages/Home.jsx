import Sidebar from "../components/Sidebar";
import ChatBox from "../components/ChatBox";

export default function Home() {

    return (

        <div className="flex h-screen bg-zinc-900 text-white">

            <Sidebar />

            <ChatBox />

        </div>

    );

}