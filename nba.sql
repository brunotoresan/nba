CREATE TABLE "teamMatches" (
  "id" SERIAL PRIMARY KEY,
  "team" text[] NOT NULL,
  "match" text[] NOT NULL,
  "date" TIMESTAMP NOT NULL,
  "won" BOOLEAN NOT NULL,
  "points" integer NOT NULL,
  "fgm" integer NOT NULL,
  "fga" integer NOT NULL,
  "fgp" float NOT NULL,
  "3pm" integer NOT NULL,
  "3pa" integer NOT NULL,
  "3pp" float NOT NULL,
  "ftm" integer NOT NULL,
  "fta" integer NOT NULL,
  "ftp" float NOT NULL,  
  "oreb" integer NOT NULL,
  "dreb" integer NOT NULL,
  "reb" integer NOT NULL,
  "ast" integer NOT NULL,
  "stl" integer NOT NULL,
  "blk" integer NOT NULL,
  "tov" integer NOT NULL
);

CREATE TABLE "playersMatches" (
  "id" SERIAL PRIMARY KEY,
  "player" text[] NOT NULL,
  "team" text[] NOT NULL,
  "match" integer NOT NULL,
  "date" TIMESTAMP NOT NULL,
  "won" BOOLEAN NOT NULL,
  "points" integer NOT NULL,
  "fgm" integer NOT NULL,
  "fga" integer NOT NULL,
  "fgp" float NOT NULL,
  "3pm" integer NOT NULL,
  "3pa" integer NOT NULL,
  "3pp" float NOT NULL,
  "ftm" integer NOT NULL,
  "fta" integer NOT NULL,
  "ftp" float NOT NULL,  
  "oreb" integer NOT NULL,
  "dreb" integer NOT NULL,
  "reb" integer NOT NULL,
  "ast" integer NOT NULL,
  "stl" integer NOT NULL,
  "blk" integer NOT NULL,
  "tov" integer NOT NULL
);

CREATE TABLE "playersShooting" (
  "player" text[] PRIMARY KEY,
  "team" text[] NOT NULL,
  "age" integer NOT NULL,
  "rar_fgm" float NOT NULL,
  "rar_fga" float NOT NULL,
  "rar_fgp" float NOT NULL,
  "itp_fgm" float NOT NULL,
  "itp_fga" float NOT NULL,
  "itp_fgp" float NOT NULL,
  "mrg_fgm" float NOT NULL,
  "mrg_fga" float NOT NULL,
  "mrg_fgp" float NOT NULL,
  "lc3_fgm" float NOT NULL,
  "lc3_fga" float NOT NULL,
  "lc3_fgp" float NOT NULL,
  "rc3_fgm" float NOT NULL,
  "rc3_fga" float NOT NULL,
  "rc3_fgp" float NOT NULL,
  "cn3_fgm" float NOT NULL,
  "cn3_fga" float NOT NULL,
  "cn3_fgp" float NOT NULL,
  "ab3_fgm" float NOT NULL,
  "ab3_fga" float NOT NULL,
  "ab3_fgp" float NOT NULL 
);

CREATE TABLE "playersInfo" (
  "player" text[] PRIMARY KEY NOT NULL,
  "team" text[] NOT NULL,
  "height" integer NOT NULL,
  "weight" integer NOT NULL
);

ALTER TABLE "playersMatches" ADD FOREIGN KEY ("match") REFERENCES "teamMatches" ("id");
ALTER TABLE "playersMatches" ADD FOREIGN KEY ("player") REFERENCES "playersShooting" ("player");
ALTER TABLE "playersMatches" ADD FOREIGN KEY ("player") REFERENCES "playersInfo" ("player");