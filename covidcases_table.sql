DROP TABLE covidcases;
CREATE TABLE IF NOT EXISTS covidcases(
    country varchar(20) NOT NULL,
    region varchar(10) NOT NULL,
    cases_total  BIGINT NOT NULL,
    cases_total_per1000 DOUBLE DEFAULT 0.0,
    cases_newly BIGINT DEFAULT 0,
    cases_newly_last7_per100000 FLOAT default 0.0,
    cases_reported_last24  INT DEFAULT 0,
    deaths BIGINT DEFAULT 0,
    deaths_reported_last7 INT DEFAULT 0,
    deaths_reported_last7_per100000  INT DEFAULT 0,
    deaths_newly_reported_in_last24hours INT DEFAULT 0,
    date_happend DATE NOT NULL
);