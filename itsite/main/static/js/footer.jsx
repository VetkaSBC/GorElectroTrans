import React from "react";
import ReactDOM from "react-dom/client";
import "../css/footer.css";
import Paragraph from "./par.jsx";
import dataFooter from "./dataFooter.js";

export const Footer = () => {
  return (
    <div className="containerfooter">
      <div className="paragraph">
      <Paragraph data={dataFooter[0]} className="text" />
      <Paragraph data={dataFooter[1]} className="text" />
      <Paragraph data={dataFooter[2]} className="text" />
      <Paragraph data={dataFooter[3]} className="text" />
      </div>
      <div className="link-footer">
          <a href="https://vk.com/spbgupget">
            <i class="fab fa-vk"></i>
          </a>
          <a href="https://t.me/getspb">
            <i class="fa-brands fa-telegram"></i>
          </a>
          <a href="https://feeds.feedburner.com/spbgupget">
            <i class="fas fa-wifi"></i>
          </a>
        </div>
    </div>
  );
};

const footerElement = document.getElementById("footer");
ReactDOM.createRoot(footerElement).render(<Footer />);

export default Footer;
