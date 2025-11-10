PRAGMA foreign_keys = ON;

-- Добавляем задачу к существующему проекту BuildTracker (id = 1)
INSERT INTO zadanie (project_id, nazwa, opis, status, start_date, end_date)
VALUES (
  1,
  'Zrób zadania',
  'Utworzone przez test.sql',
  'zaplanowano',
  '2020-05-08 00:00:00',
  '2020-05-10 00:00:00'
);
