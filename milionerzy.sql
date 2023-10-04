-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 04 Paź 2023, 12:03
-- Wersja serwera: 10.4.27-MariaDB
-- Wersja PHP: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `milionerzy`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `odp`
--

CREATE TABLE `odp` (
  `id1` int(11) NOT NULL,
  `A` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `B` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `C` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `D` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `Poprawna_odp` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Zrzut danych tabeli `odp`
--

INSERT INTO `odp` (`id1`, `A`, `B`, `C`, `D`, `Poprawna_odp`) VALUES
(1, '4', '6', '8', '2', '6'),
(2, 'Francuski', 'Argentyński', 'Hiszpański', 'Angielski', 'Hiszpański'),
(3, 'górską kolejką', 'wyciągiem krzesełkowym', 'końskim zaprzęgiem', 'wyciągiem orczykowym', 'końskim zaprzęgiem'),
(4, 'Adam Mickiewicz', 'Jan Kochanowski', 'Jan Brzechwa', 'Henryk Sienkiewicz', 'Jan Kochanowski'),
(5, 'poślubił wieśniaczkę', 'przekazał władzę synowi', 'rozdał majątek ludowi', 'ukorzył się przed papieżem', 'ukorzył się przed papieżem'),
(6, 'skrzyżowany z kielnią', 'wystający spod cyrkla', 'spoczywający na księdze', 'pneumatyczny', 'wystający spod cyrkla'),
(7, 'kaczy', 'indyczy', 'orli', 'perliczy', 'kaczy'),
(8, 'postojowych', 'przystankowych', 'przerywnikowych', 'przestankowych', 'przestankowych'),
(9, 'Czapką, papką i solą', 'Skórą, furą i komórą', 'Poglądów kontrolą', 'Wszystkim, na co pozwolą', 'Czapką, papką i solą'),
(10, 'Frankfurt', 'Hamburg', 'Berlin', 'Wilno', 'Beriln'),
(11, 'Ameryka Północna', 'Afryka', 'Europa', 'Azja', 'Afryka'),
(12, 'Battlefield', 'Cs:go', 'NeedForSpeed', 'Valorant', 'NeedForSpeed'),
(13, '85% czerwony, 48% zielony, 12% niebieski', '12% czerwony, 36% zielony, 79% niebieski', '21% czerwony, 69% zielony, 37% niebieski', '54% czerwony, 23% zielony, 78% niebieski', '85% czerwony, 48% zielony, 12% niebieski');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pyt`
--

CREATE TABLE `pyt` (
  `id` int(11) NOT NULL,
  `Pytania` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Zrzut danych tabeli `pyt`
--

INSERT INTO `pyt` (`id`, `Pytania`) VALUES
(1, 'Ile wynosi wynik 2+2*2?'),
(2, 'Jaki język jest urzędowym w Argentynie?'),
(3, 'Kto wjechał na górę fasiągiem, dostał się tam?'),
(4, 'Kto napisał treny?'),
(5, 'Co takiego zrobił cesarz Henryk IV we włoskiej Canossie, że historia ta zakorzeniła się w języku?'),
(6, 'Godłem ZSRR były skrzyżowane sierp i młot, a godłem NRD młot?'),
(7, 'Dziób dziobaka australijskiego przypomina kształtem ten?'),
(8, 'Kropka, przecinek i średnik to przykłady znaków?'),
(9, 'Czym według staropolskiego przysłowia ludzie ludzi niewolą?'),
(10, 'Jakie miasto jest stolica Niemiec?'),
(11, 'Na jakim kontynencie leży Namibia?'),
(12, 'Która z gier nie jest strzelanką?'),
(13, 'Z jakich kolorów utworzysz kolor ugier w modelu RGB?');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `odp`
--
ALTER TABLE `odp`
  ADD PRIMARY KEY (`id1`);

--
-- Indeksy dla tabeli `pyt`
--
ALTER TABLE `pyt`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `odp`
--
ALTER TABLE `odp`
  MODIFY `id1` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT dla tabeli `pyt`
--
ALTER TABLE `pyt`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
