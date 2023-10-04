-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Paź 04, 2023 at 07:41 PM
-- Wersja serwera: 10.4.28-MariaDB
-- Wersja PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `milionerzy`
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
-- Dumping data for table `odp`
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
(13, '85% czerwony, 48% zielony, 12% niebieski', '12% czerwony, 36% zielony, 79% niebieski', '21% czerwony, 69% zielony, 37% niebieski', '54% czerwony, 23% zielony, 78% niebieski', '85% czerwony, 48% zielony, 12% niebieski'),
(14, 'miłości', 'śmierci', 'zazdrości', 'uwielbienie', 'zazdrości'),
(15, '2008', '2009', '2007', '2006', '2009'),
(16, 'Andrzej Pazura', 'Hubert Urbański', 'Katarzyna Dowbor', 'Elżbieta Romanowska', 'Elżbieta Romanowska'),
(17, 'Edward Lutczyn', 'Marek Raczkowski', 'Henryk Sawka', 'Andrzej Mleczko', 'Edward Lutczyn'),
(18, 'Ze złota', 'Ze srebra', 'Z brązu', 'Z żeliwa', 'Ze srebra'),
(19, 'pod austriacki', 'nie trafił pod żaden', 'pod pruski', 'pod rosyjski', 'pod pruski'),
(20, 'Minecraft', 'Counter-Strike: Global Offensive', 'The Forest', 'Terraria', 'Terraria'),
(21, 'rękochwytki', 'nogogłaszczki', 'łapkomyjki', 'zębołapki', 'nogogłaszczki'),
(22, 'po francusku', 'po grecku', 'po rosyjsku', 'po włosku', 'po francusku'),
(23, 'w więzieniach', 'w sklepach', 'na przystankach', 'w szkołach', 'w więzieniach'),
(24, 'bezprzewodowa sieć globalna', 'bezprzewodowa sieć lokalna', 'sieć globalna', 'sieć lokalna', 'bezprzewodowa sieć lokalna'),
(25, 'Ac', 'As', 'Sb', 'Hf', 'Sb'),
(26, 'C', 'V', 'Cu', 'Al', 'C'),
(27, 'Oceania', 'Ameryka Południowa', 'Afryka', 'Azja', 'Azja'),
(28, '1415', '1400', '1410', '1420', '1410'),
(29, 'po Darku\"', 'po Halinie\"', 'po Marku\"', 'po Czarku\"', 'po Halinie\"'),
(30, 'Isaac Hayes', 'Smokey Robinson', 'Marvin Gay', 'James Brown', 'Isaac Hayes'),
(31, 'wałek', 'tłuczek', 'dzban', 'blat', 'wałek'),
(32, '15 lat', '10 lat', '5 lat', '20 lat', '10 lat'),
(33, 'polerska', 'cukrowa', 'do kanapek', 'do butów', 'do kanapek'),
(34, 'strajkiem', 'narzucaniem danych poglądów', 'wyborami', 'zawodami', 'narzucaniem danych poglądów'),
(35, '1972', '1971', '1970', '1973', '1970'),
(36, 'z bulimią', 'z anoreksją', 'z alkoholizmem', 'z artretyzmem', 'z alkoholizmem'),
(37, 'Arab', 'W Szwajcarii', 'Anhelli', 'Godzina myśli', 'Anhelli'),
(38, 'to monarchie parlamentarne', 'ich stolice leżą nad morzem', 'mają identyczne PKB per capita', 'przechodzi przez nie równik', 'przechodzi przez nie równik'),
(39, 'Lusaka', 'Harare', 'Ułan Bator', 'Bagdad', 'Lusaka'),
(40, 'Wietnam', 'Watykan', 'Lesotho', 'Namibia', 'Watykan'),
(41, 'Norwegię z Danią', 'Szwecję z Finlandią', 'Danię ze Szwecją', 'Finlandię z Estonią', 'Danię ze Szwecją'),
(42, '(a+b)*h', 'a*h', 'a*h/2', '(a+b)*h/2', '(a+b)*h/2'),
(43, 'Kubuś uszatek', 'Kubuś puchatek', 'Myszka Miki', 'Stitch ', 'Kubuś puchatek'),
(44, '\"Barbie\"', '\"Oppenheimer\"', '\"Spider-Man: Poprzez multiwersum\"', '\"Porady na zdrady 2\"', '\"Spider-Man: Poprzez multiwersum\"'),
(45, 'w myślistwie', 'na wieży mariackiej', 'w korporacjach', 'w polityce', 'w myślistwie'),
(46, 'po I wojnie światowej', 'po II wojnie światowej', 'po wojnie indochińskiej', 'po wojnie secesyjnej', 'po II wojnie światowej'),
(47, 'sportowych Au', 'wszystkiego wszędzie i zawsze', 'prowadnic', 'ludzi, zwłaszcza podejrzane', 'ludzi, zwłaszcza podejrzane'),
(48, 'grasica', 'nadnercze', 'trzustka', 'szyszynka', 'trzustka');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pyt`
--

CREATE TABLE `pyt` (
  `id` int(11) NOT NULL,
  `Pytania` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pyt`
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
(13, 'Z jakich kolorów utworzysz kolor ugier w modelu RGB?'),
(14, 'Czego alegorią jest żółta róża?'),
(15, 'W którym roku powstała gra League of Legends?'),
(16, 'Kto jest prowadzącym popularnego programu \"Nasz nowy dom\"?'),
(17, 'Kto jest twórcą logo zespołu Perfect??'),
(18, 'Z czego odlane są złote medale olimpijskie??'),
(19, 'Pod jaki zabór trafił Białystok w 1795 r., jeśli trafił??'),
(20, 'Która z gier została oficjalnie wydana jako pierwsza?'),
(21, 'Druga para odnóży gębowych pajęczaków, która służy do rozdrabniania pokarmów i jako narządy dotykowe, to...?'),
(22, 'W Polsce wchodzimy po angielsku. Po jakiemu wchodzą Anglicy??'),
(23, 'Gdzie najczęściej można spotkać aparaty słuchowe telefoniczne samoinkasujące??'),
(24, 'Czym jest WLAN?'),
(25, 'Jakim symbolem oznaczamy pierwiastek chemiczny antymon?'),
(26, 'Który z pierwiastków nie jest metalem?'),
(27, 'Na jakim kontynencie leży Laos?'),
(28, 'W którym roku rozegrała się bitwa pod Grunwaldem?'),
(29, 'Agnieszka Osiecka w piosence \"Aspiryna blues\" napisała, że \"Ludzie mają cudne sny po kokainie i po winie, po chininie...'),
(30, 'Który z legendarnych wokalistów soulowych użyczył głosu kucharzowi ze szkolnej stołówki w serialu animowanym \"Miasteczko South Park\"?'),
(31, 'Kuchenny synonim przekrętu...'),
(32, 'Jaka jest średnia wieku w grupie składającej się z trzech 4-latków, czterech 11-latków, dwóch 12-latków i jednego 20-latka?'),
(33, 'Awanturka to pasta...'),
(34, 'Czym jest propaganda?'),
(35, 'W którym roku Edward Gierek został 1 sekretarzem KC PZPR'),
(36, 'Z jaką chorobą zmaga się norweski policjant Harry Hole w serii kryminałów Jo Nesbo?'),
(37, 'Który utwór Juliusza Słowackiego napisany jest prozą?'),
(38, 'Co łączy Brazylię, Indonezję i Kenię?'),
(39, 'Jakie miasto jest stolica Zambii?'),
(40, 'Które państwo jest najmniejsze'),
(41, 'Most nad Sundem łączy'),
(42, 'Jaki jest wzór na pole trapezu?'),
(43, 'O której postaci powstał horror?'),
(44, 'Który film nie miał premiery w wakacje 2023?'),
(45, 'Sygnałówka to trąbka sygnalistów. Gdzie?'),
(46, 'Bezpośrednio po której z wojen powstał UNICEF, żeby zapewnić żywotność i opiekę zdrowotną dla dzieci i matek?'),
(47, 'Konduita to prowadzenie się'),
(48, 'Który z gruczołów wydziela sok trawienny?');

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
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `odp`
--
ALTER TABLE `odp`
  MODIFY `id1` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `pyt`
--
ALTER TABLE `pyt`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
