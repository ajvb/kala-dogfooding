CREATE TABLE links (
    rss_feed_title TEXT,
    rss_feed_link TEXT,

    title TEXT NOT NULL,
    link TEXT NOT NULL,
    published TIMESTAMP NOT NULL,

    created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
);
