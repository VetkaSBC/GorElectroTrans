import React from "react";
import ReactDOM from "react-dom/client"; // Используем react-dom/client
import logo from "../img/logo.png";
import logoR from "../img/headerparv.png";
import "../css/header.css";

const Header = () => {
  return (
    <div className="containerhead">
      <a href="https://electrotrans.spb.ru">
        <img src={logo} alt="" className="img" />
      </a>
      <div className="text-cont-head">
        <h1>Всем по пути</h1>
      </div>
      <div className="right">
        <a href="https://getmuseum.ru">
          <img src={logoR} alt="" className="img" />
        </a>
      </div>
    </div>
  );
};

// Создаем корневой элемент для рендеринга заголовка
const headerElement = document.getElementById("header");
// Рендерим компонент Header в корневой элемент
ReactDOM.createRoot(headerElement).render(<Header />);

export default Header;