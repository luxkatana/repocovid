CREATE TABLE IF NOT EXISTS covidcases(
    country varchar(20) NOT NULL,
    region varchar(10) NOT NULL,
    cases_total  BIGINT NOT NULL,
    cases_total_per1000 DOUBLE NOT NULL,
    cases_newly BIGINT NOT NULL,
    cases_newly_last7_per100000 FLOAT NOT NULL,
    cases_reported_last24  INT NOT NULL,
    deaths BIGINT NOT NULL,
    deaths_reported_last7 INT NOT NULL,
    deaths_reported_last7_per100000  INT NOT NULL,
    deaths_newly_reported_in_last24hours INT NOT NULL
);