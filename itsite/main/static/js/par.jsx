import React from "react";
import ReactDOM from "react-dom/client";
import "../css/par.css";

export const Paragraph = (data) => {

    const htmlParagraphs = data.data.paragraphs.map((paragraph, index) => {
        return <div key={index}><a href={paragraph.link}>{paragraph.name}</a></div>
    });

    return (
        <div className="text-cont">
            <h1>{data.data.title}</h1>
            <ul>
              {htmlParagraphs}
            </ul>
        </div>
    );
};

export default Paragraph;