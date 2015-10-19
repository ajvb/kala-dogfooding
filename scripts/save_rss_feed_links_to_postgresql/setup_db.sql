CREATE DATABASE save_rss_feeds;
CREATE ROLE save_rss_feeds WITH PASSWORD 'save_rss_feeds';
ALTER ROLE save_rss_feeds LOGIN;
ALTER ROLE save_rss_feeds WITH SUPERUSER;
