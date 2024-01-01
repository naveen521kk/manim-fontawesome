# Automatically generated using scripts/update.py. Don't edit.

# Copyright Naveen M K
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE.txt file.

import os

from pathlib import Path
from enum import Enum
from manim import SVGMobject, config, BLACK, WHITE

__all__ = ["brand", "regular", "solid", "FONT_AWESOME_VERSION"]

svg_dir = Path(__file__).parent / 'font-awesome'/ 'svgs'
brand_dir = svg_dir / 'brands'
regular_dir = svg_dir / 'regular'
solid_dir = svg_dir / 'solid'
FONT_AWESOME_VERSION = '6.5.1'


class _Brand(Enum):
  
    hotjar = os.fspath(brand_dir / 'hotjar.svg')
  
    dev = os.fspath(brand_dir / 'dev.svg')
  
    stumbleupon = os.fspath(brand_dir / 'stumbleupon.svg')
  
    mixcloud = os.fspath(brand_dir / 'mixcloud.svg')
  
    shopify = os.fspath(brand_dir / 'shopify.svg')
  
    sistrix = os.fspath(brand_dir / 'sistrix.svg')
  
    autoprefixer = os.fspath(brand_dir / 'autoprefixer.svg')
  
    renren = os.fspath(brand_dir / 'renren.svg')
  
    medium = os.fspath(brand_dir / 'medium.svg')
  
    yandex_international = os.fspath(brand_dir / 'yandex-international.svg')
  
    git = os.fspath(brand_dir / 'git.svg')
  
    freebsd = os.fspath(brand_dir / 'freebsd.svg')
  
    nfc_directional = os.fspath(brand_dir / 'nfc-directional.svg')
  
    digg = os.fspath(brand_dir / 'digg.svg')
  
    creative_commons_remix = os.fspath(brand_dir / 'creative-commons-remix.svg')
  
    quora = os.fspath(brand_dir / 'quora.svg')
  
    ideal = os.fspath(brand_dir / 'ideal.svg')
  
    stumbleupon_circle = os.fspath(brand_dir / 'stumbleupon-circle.svg')
  
    html5 = os.fspath(brand_dir / 'html5.svg')
  
    schlix = os.fspath(brand_dir / 'schlix.svg')
  
    square_youtube = os.fspath(brand_dir / 'square-youtube.svg')
  
    buffer = os.fspath(brand_dir / 'buffer.svg')
  
    rockrms = os.fspath(brand_dir / 'rockrms.svg')
  
    github_alt = os.fspath(brand_dir / 'github-alt.svg')
  
    laravel = os.fspath(brand_dir / 'laravel.svg')
  
    symfony = os.fspath(brand_dir / 'symfony.svg')
  
    yammer = os.fspath(brand_dir / 'yammer.svg')
  
    airbnb = os.fspath(brand_dir / 'airbnb.svg')
  
    padlet = os.fspath(brand_dir / 'padlet.svg')
  
    centos = os.fspath(brand_dir / 'centos.svg')
  
    grunt = os.fspath(brand_dir / 'grunt.svg')
  
    mandalorian = os.fspath(brand_dir / 'mandalorian.svg')
  
    hooli = os.fspath(brand_dir / 'hooli.svg')
  
    first_order_alt = os.fspath(brand_dir / 'first-order-alt.svg')
  
    gg_circle = os.fspath(brand_dir / 'gg-circle.svg')
  
    _42_group = os.fspath(brand_dir / '42-group.svg')
  
    uber = os.fspath(brand_dir / 'uber.svg')
  
    envira = os.fspath(brand_dir / 'envira.svg')
  
    square_whatsapp = os.fspath(brand_dir / 'square-whatsapp.svg')
  
    ubuntu = os.fspath(brand_dir / 'ubuntu.svg')
  
    ebay = os.fspath(brand_dir / 'ebay.svg')
  
    square_tumblr = os.fspath(brand_dir / 'square-tumblr.svg')
  
    typo3 = os.fspath(brand_dir / 'typo3.svg')
  
    vnv = os.fspath(brand_dir / 'vnv.svg')
  
    jedi_order = os.fspath(brand_dir / 'jedi-order.svg')
  
    bluetooth_b = os.fspath(brand_dir / 'bluetooth-b.svg')
  
    phabricator = os.fspath(brand_dir / 'phabricator.svg')
  
    square_pied_piper = os.fspath(brand_dir / 'square-pied-piper.svg')
  
    kickstarter = os.fspath(brand_dir / 'kickstarter.svg')
  
    creative_commons_pd_alt = os.fspath(brand_dir / 'creative-commons-pd-alt.svg')
  
    fedex = os.fspath(brand_dir / 'fedex.svg')
  
    wordpress = os.fspath(brand_dir / 'wordpress.svg')
  
    unsplash = os.fspath(brand_dir / 'unsplash.svg')
  
    free_code_camp = os.fspath(brand_dir / 'free-code-camp.svg')
  
    goodreads = os.fspath(brand_dir / 'goodreads.svg')
  
    square_vimeo = os.fspath(brand_dir / 'square-vimeo.svg')
  
    whatsapp = os.fspath(brand_dir / 'whatsapp.svg')
  
    safari = os.fspath(brand_dir / 'safari.svg')
  
    google_scholar = os.fspath(brand_dir / 'google-scholar.svg')
  
    tumblr = os.fspath(brand_dir / 'tumblr.svg')
  
    google_pay = os.fspath(brand_dir / 'google-pay.svg')
  
    avianex = os.fspath(brand_dir / 'avianex.svg')
  
    fulcrum = os.fspath(brand_dir / 'fulcrum.svg')
  
    themeco = os.fspath(brand_dir / 'themeco.svg')
  
    unity = os.fspath(brand_dir / 'unity.svg')
  
    mintbit = os.fspath(brand_dir / 'mintbit.svg')
  
    square_reddit = os.fspath(brand_dir / 'square-reddit.svg')
  
    reddit_alien = os.fspath(brand_dir / 'reddit-alien.svg')
  
    pushed = os.fspath(brand_dir / 'pushed.svg')
  
    wpbeginner = os.fspath(brand_dir / 'wpbeginner.svg')
  
    uniregistry = os.fspath(brand_dir / 'uniregistry.svg')
  
    signal_messenger = os.fspath(brand_dir / 'signal-messenger.svg')
  
    jira = os.fspath(brand_dir / 'jira.svg')
  
    cc_mastercard = os.fspath(brand_dir / 'cc-mastercard.svg')
  
    buromobelexperte = os.fspath(brand_dir / 'buromobelexperte.svg')
  
    mastodon = os.fspath(brand_dir / 'mastodon.svg')
  
    google_play = os.fspath(brand_dir / 'google-play.svg')
  
    nimblr = os.fspath(brand_dir / 'nimblr.svg')
  
    btc = os.fspath(brand_dir / 'btc.svg')
  
    webflow = os.fspath(brand_dir / 'webflow.svg')
  
    resolving = os.fspath(brand_dir / 'resolving.svg')
  
    atlassian = os.fspath(brand_dir / 'atlassian.svg')
  
    magento = os.fspath(brand_dir / 'magento.svg')
  
    battle_net = os.fspath(brand_dir / 'battle-net.svg')
  
    medapps = os.fspath(brand_dir / 'medapps.svg')
  
    neos = os.fspath(brand_dir / 'neos.svg')
  
    twitch = os.fspath(brand_dir / 'twitch.svg')
  
    linkedin_in = os.fspath(brand_dir / 'linkedin-in.svg')
  
    readme = os.fspath(brand_dir / 'readme.svg')
  
    palfed = os.fspath(brand_dir / 'palfed.svg')
  
    creative_commons_nd = os.fspath(brand_dir / 'creative-commons-nd.svg')
  
    square_steam = os.fspath(brand_dir / 'square-steam.svg')
  
    keybase = os.fspath(brand_dir / 'keybase.svg')
  
    asymmetrik = os.fspath(brand_dir / 'asymmetrik.svg')
  
    sellsy = os.fspath(brand_dir / 'sellsy.svg')
  
    think_peaks = os.fspath(brand_dir / 'think-peaks.svg')
  
    flickr = os.fspath(brand_dir / 'flickr.svg')
  
    watchman_monitoring = os.fspath(brand_dir / 'watchman-monitoring.svg')
  
    scribd = os.fspath(brand_dir / 'scribd.svg')
  
    squarespace = os.fspath(brand_dir / 'squarespace.svg')
  
    spotify = os.fspath(brand_dir / 'spotify.svg')
  
    css3_alt = os.fspath(brand_dir / 'css3-alt.svg')
  
    bandcamp = os.fspath(brand_dir / 'bandcamp.svg')
  
    square_pinterest = os.fspath(brand_dir / 'square-pinterest.svg')
  
    facebook = os.fspath(brand_dir / 'facebook.svg')
  
    square_x_twitter = os.fspath(brand_dir / 'square-x-twitter.svg')
  
    yahoo = os.fspath(brand_dir / 'yahoo.svg')
  
    facebook_messenger = os.fspath(brand_dir / 'facebook-messenger.svg')
  
    square_viadeo = os.fspath(brand_dir / 'square-viadeo.svg')
  
    rocketchat = os.fspath(brand_dir / 'rocketchat.svg')
  
    square_google_plus = os.fspath(brand_dir / 'square-google-plus.svg')
  
    erlang = os.fspath(brand_dir / 'erlang.svg')
  
    python = os.fspath(brand_dir / 'python.svg')
  
    gitter = os.fspath(brand_dir / 'gitter.svg')
  
    fonticons_fi = os.fspath(brand_dir / 'fonticons-fi.svg')
  
    sitrox = os.fspath(brand_dir / 'sitrox.svg')
  
    debian = os.fspath(brand_dir / 'debian.svg')
  
    uncharted = os.fspath(brand_dir / 'uncharted.svg')
  
    weixin = os.fspath(brand_dir / 'weixin.svg')
  
    slideshare = os.fspath(brand_dir / 'slideshare.svg')
  
    houzz = os.fspath(brand_dir / 'houzz.svg')
  
    wpforms = os.fspath(brand_dir / 'wpforms.svg')
  
    foursquare = os.fspath(brand_dir / 'foursquare.svg')
  
    evernote = os.fspath(brand_dir / 'evernote.svg')
  
    fonticons = os.fspath(brand_dir / 'fonticons.svg')
  
    ioxhost = os.fspath(brand_dir / 'ioxhost.svg')
  
    codiepie = os.fspath(brand_dir / 'codiepie.svg')
  
    google_plus_g = os.fspath(brand_dir / 'google-plus-g.svg')
  
    xing = os.fspath(brand_dir / 'xing.svg')
  
    gulp = os.fspath(brand_dir / 'gulp.svg')
  
    instalod = os.fspath(brand_dir / 'instalod.svg')
  
    chrome = os.fspath(brand_dir / 'chrome.svg')
  
    buysellads = os.fspath(brand_dir / 'buysellads.svg')
  
    mailchimp = os.fspath(brand_dir / 'mailchimp.svg')
  
    ussunnah = os.fspath(brand_dir / 'ussunnah.svg')
  
    aws = os.fspath(brand_dir / 'aws.svg')
  
    square_letterboxd = os.fspath(brand_dir / 'square-letterboxd.svg')
  
    openid = os.fspath(brand_dir / 'openid.svg')
  
    opencart = os.fspath(brand_dir / 'opencart.svg')
  
    reacteurope = os.fspath(brand_dir / 'reacteurope.svg')
  
    shopware = os.fspath(brand_dir / 'shopware.svg')
  
    digital_ocean = os.fspath(brand_dir / 'digital-ocean.svg')
  
    searchengin = os.fspath(brand_dir / 'searchengin.svg')
  
    deploydog = os.fspath(brand_dir / 'deploydog.svg')
  
    trade_federation = os.fspath(brand_dir / 'trade-federation.svg')
  
    d_and_d = os.fspath(brand_dir / 'd-and-d.svg')
  
    quinscape = os.fspath(brand_dir / 'quinscape.svg')
  
    critical_role = os.fspath(brand_dir / 'critical-role.svg')
  
    pagelines = os.fspath(brand_dir / 'pagelines.svg')
  
    delicious = os.fspath(brand_dir / 'delicious.svg')
  
    amilia = os.fspath(brand_dir / 'amilia.svg')
  
    nfc_symbol = os.fspath(brand_dir / 'nfc-symbol.svg')
  
    shoelace = os.fspath(brand_dir / 'shoelace.svg')
  
    microsoft = os.fspath(brand_dir / 'microsoft.svg')
  
    wpressr = os.fspath(brand_dir / 'wpressr.svg')
  
    square_odnoklassniki = os.fspath(brand_dir / 'square-odnoklassniki.svg')
  
    osi = os.fspath(brand_dir / 'osi.svg')
  
    usb = os.fspath(brand_dir / 'usb.svg')
  
    mendeley = os.fspath(brand_dir / 'mendeley.svg')
  
    creative_commons_pd = os.fspath(brand_dir / 'creative-commons-pd.svg')
  
    bimobject = os.fspath(brand_dir / 'bimobject.svg')
  
    dyalog = os.fspath(brand_dir / 'dyalog.svg')
  
    angrycreative = os.fspath(brand_dir / 'angrycreative.svg')
  
    patreon = os.fspath(brand_dir / 'patreon.svg')
  
    glide_g = os.fspath(brand_dir / 'glide-g.svg')
  
    blackberry = os.fspath(brand_dir / 'blackberry.svg')
  
    strava = os.fspath(brand_dir / 'strava.svg')
  
    x_twitter = os.fspath(brand_dir / 'x-twitter.svg')
  
    mix = os.fspath(brand_dir / 'mix.svg')
  
    periscope = os.fspath(brand_dir / 'periscope.svg')
  
    earlybirds = os.fspath(brand_dir / 'earlybirds.svg')
  
    itunes_note = os.fspath(brand_dir / 'itunes-note.svg')
  
    affiliatetheme = os.fspath(brand_dir / 'affiliatetheme.svg')
  
    xbox = os.fspath(brand_dir / 'xbox.svg')
  
    suse = os.fspath(brand_dir / 'suse.svg')
  
    linkedin = os.fspath(brand_dir / 'linkedin.svg')
  
    creative_commons_by = os.fspath(brand_dir / 'creative-commons-by.svg')
  
    jsfiddle = os.fspath(brand_dir / 'jsfiddle.svg')
  
    orcid = os.fspath(brand_dir / 'orcid.svg')
  
    font_awesome = os.fspath(brand_dir / 'font-awesome.svg')
  
    stack_exchange = os.fspath(brand_dir / 'stack-exchange.svg')
  
    cc_amazon_pay = os.fspath(brand_dir / 'cc-amazon-pay.svg')
  
    raspberry_pi = os.fspath(brand_dir / 'raspberry-pi.svg')
  
    angular = os.fspath(brand_dir / 'angular.svg')
  
    square_facebook = os.fspath(brand_dir / 'square-facebook.svg')
  
    gratipay = os.fspath(brand_dir / 'gratipay.svg')
  
    wikipedia_w = os.fspath(brand_dir / 'wikipedia-w.svg')
  
    node = os.fspath(brand_dir / 'node.svg')
  
    lyft = os.fspath(brand_dir / 'lyft.svg')
  
    studiovinari = os.fspath(brand_dir / 'studiovinari.svg')
  
    mizuni = os.fspath(brand_dir / 'mizuni.svg')
  
    buy_n_large = os.fspath(brand_dir / 'buy-n-large.svg')
  
    cloudflare = os.fspath(brand_dir / 'cloudflare.svg')
  
    creative_commons_nc_jp = os.fspath(brand_dir / 'creative-commons-nc-jp.svg')
  
    react = os.fspath(brand_dir / 'react.svg')
  
    pix = os.fspath(brand_dir / 'pix.svg')
  
    viadeo = os.fspath(brand_dir / 'viadeo.svg')
  
    mixer = os.fspath(brand_dir / 'mixer.svg')
  
    viacoin = os.fspath(brand_dir / 'viacoin.svg')
  
    pied_piper_alt = os.fspath(brand_dir / 'pied-piper-alt.svg')
  
    firefox_browser = os.fspath(brand_dir / 'firefox-browser.svg')
  
    whmcs = os.fspath(brand_dir / 'whmcs.svg')
  
    vuejs = os.fspath(brand_dir / 'vuejs.svg')
  
    apple = os.fspath(brand_dir / 'apple.svg')
  
    amazon_pay = os.fspath(brand_dir / 'amazon-pay.svg')
  
    optin_monster = os.fspath(brand_dir / 'optin-monster.svg')
  
    joget = os.fspath(brand_dir / 'joget.svg')
  
    square_js = os.fspath(brand_dir / 'square-js.svg')
  
    deskpro = os.fspath(brand_dir / 'deskpro.svg')
  
    android = os.fspath(brand_dir / 'android.svg')
  
    hubspot = os.fspath(brand_dir / 'hubspot.svg')
  
    confluence = os.fspath(brand_dir / 'confluence.svg')
  
    facebook_f = os.fspath(brand_dir / 'facebook-f.svg')
  
    meetup = os.fspath(brand_dir / 'meetup.svg')
  
    fly = os.fspath(brand_dir / 'fly.svg')
  
    square_gitlab = os.fspath(brand_dir / 'square-gitlab.svg')
  
    fedora = os.fspath(brand_dir / 'fedora.svg')
  
    centercode = os.fspath(brand_dir / 'centercode.svg')
  
    twitter = os.fspath(brand_dir / 'twitter.svg')
  
    etsy = os.fspath(brand_dir / 'etsy.svg')
  
    fort_awesome_alt = os.fspath(brand_dir / 'fort-awesome-alt.svg')
  
    sticker_mule = os.fspath(brand_dir / 'sticker-mule.svg')
  
    square_behance = os.fspath(brand_dir / 'square-behance.svg')
  
    weibo = os.fspath(brand_dir / 'weibo.svg')
  
    chromecast = os.fspath(brand_dir / 'chromecast.svg')
  
    bitbucket = os.fspath(brand_dir / 'bitbucket.svg')
  
    wodu = os.fspath(brand_dir / 'wodu.svg')
  
    superpowers = os.fspath(brand_dir / 'superpowers.svg')
  
    instagram = os.fspath(brand_dir / 'instagram.svg')
  
    square_twitter = os.fspath(brand_dir / 'square-twitter.svg')
  
    cc_diners_club = os.fspath(brand_dir / 'cc-diners-club.svg')
  
    wizards_of_the_coast = os.fspath(brand_dir / 'wizards-of-the-coast.svg')
  
    dribbble = os.fspath(brand_dir / 'dribbble.svg')
  
    less = os.fspath(brand_dir / 'less.svg')
  
    contao = os.fspath(brand_dir / 'contao.svg')
  
    ello = os.fspath(brand_dir / 'ello.svg')
  
    d_and_d_beyond = os.fspath(brand_dir / 'd-and-d-beyond.svg')
  
    pinterest = os.fspath(brand_dir / 'pinterest.svg')
  
    markdown = os.fspath(brand_dir / 'markdown.svg')
  
    medrt = os.fspath(brand_dir / 'medrt.svg')
  
    square_font_awesome = os.fspath(brand_dir / 'square-font-awesome.svg')
  
    hashnode = os.fspath(brand_dir / 'hashnode.svg')
  
    microblog = os.fspath(brand_dir / 'microblog.svg')
  
    github = os.fspath(brand_dir / 'github.svg')
  
    sass = os.fspath(brand_dir / 'sass.svg')
  
    staylinked = os.fspath(brand_dir / 'staylinked.svg')
  
    hornbill = os.fspath(brand_dir / 'hornbill.svg')
  
    paypal = os.fspath(brand_dir / 'paypal.svg')
  
    linux = os.fspath(brand_dir / 'linux.svg')
  
    bilibili = os.fspath(brand_dir / 'bilibili.svg')
  
    aviato = os.fspath(brand_dir / 'aviato.svg')
  
    edge = os.fspath(brand_dir / 'edge.svg')
  
    creative_commons_sa = os.fspath(brand_dir / 'creative-commons-sa.svg')
  
    blogger_b = os.fspath(brand_dir / 'blogger-b.svg')
  
    square_hacker_news = os.fspath(brand_dir / 'square-hacker-news.svg')
  
    stackpath = os.fspath(brand_dir / 'stackpath.svg')
  
    tencent_weibo = os.fspath(brand_dir / 'tencent-weibo.svg')
  
    google = os.fspath(brand_dir / 'google.svg')
  
    first_order = os.fspath(brand_dir / 'first-order.svg')
  
    cc_amex = os.fspath(brand_dir / 'cc-amex.svg')
  
    monero = os.fspath(brand_dir / 'monero.svg')
  
    playstation = os.fspath(brand_dir / 'playstation.svg')
  
    yoast = os.fspath(brand_dir / 'yoast.svg')
  
    windows = os.fspath(brand_dir / 'windows.svg')
  
    forumbee = os.fspath(brand_dir / 'forumbee.svg')
  
    bluetooth = os.fspath(brand_dir / 'bluetooth.svg')
  
    black_tie = os.fspath(brand_dir / 'black-tie.svg')
  
    sellcast = os.fspath(brand_dir / 'sellcast.svg')
  
    creative_commons_sampling_plus = os.fspath(brand_dir / 'creative-commons-sampling-plus.svg')
  
    ns8 = os.fspath(brand_dir / 'ns8.svg')
  
    vimeo_v = os.fspath(brand_dir / 'vimeo-v.svg')
  
    y_combinator = os.fspath(brand_dir / 'y-combinator.svg')
  
    imdb = os.fspath(brand_dir / 'imdb.svg')
  
    vaadin = os.fspath(brand_dir / 'vaadin.svg')
  
    hackerrank = os.fspath(brand_dir / 'hackerrank.svg')
  
    adn = os.fspath(brand_dir / 'adn.svg')
  
    linode = os.fspath(brand_dir / 'linode.svg')
  
    creative_commons = os.fspath(brand_dir / 'creative-commons.svg')
  
    edge_legacy = os.fspath(brand_dir / 'edge-legacy.svg')
  
    product_hunt = os.fspath(brand_dir / 'product-hunt.svg')
  
    firstdraft = os.fspath(brand_dir / 'firstdraft.svg')
  
    replyd = os.fspath(brand_dir / 'replyd.svg')
  
    trello = os.fspath(brand_dir / 'trello.svg')
  
    invision = os.fspath(brand_dir / 'invision.svg')
  
    diaspora = os.fspath(brand_dir / 'diaspora.svg')
  
    keycdn = os.fspath(brand_dir / 'keycdn.svg')
  
    sith = os.fspath(brand_dir / 'sith.svg')
  
    intercom = os.fspath(brand_dir / 'intercom.svg')
  
    perbyte = os.fspath(brand_dir / 'perbyte.svg')
  
    node_js = os.fspath(brand_dir / 'node-js.svg')
  
    drupal = os.fspath(brand_dir / 'drupal.svg')
  
    brave = os.fspath(brand_dir / 'brave.svg')
  
    ups = os.fspath(brand_dir / 'ups.svg')
  
    cc_discover = os.fspath(brand_dir / 'cc-discover.svg')
  
    pied_piper = os.fspath(brand_dir / 'pied-piper.svg')
  
    korvue = os.fspath(brand_dir / 'korvue.svg')
  
    apple_pay = os.fspath(brand_dir / 'apple-pay.svg')
  
    rust = os.fspath(brand_dir / 'rust.svg')
  
    pied_piper_pp = os.fspath(brand_dir / 'pied-piper-pp.svg')
  
    internet_explorer = os.fspath(brand_dir / 'internet-explorer.svg')
  
    dochub = os.fspath(brand_dir / 'dochub.svg')
  
    cmplid = os.fspath(brand_dir / 'cmplid.svg')
  
    algolia = os.fspath(brand_dir / 'algolia.svg')
  
    deviantart = os.fspath(brand_dir / 'deviantart.svg')
  
    angellist = os.fspath(brand_dir / 'angellist.svg')
  
    galactic_senate = os.fspath(brand_dir / 'galactic-senate.svg')
  
    skyatlas = os.fspath(brand_dir / 'skyatlas.svg')
  
    soundcloud = os.fspath(brand_dir / 'soundcloud.svg')
  
    supple = os.fspath(brand_dir / 'supple.svg')
  
    vk = os.fspath(brand_dir / 'vk.svg')
  
    discourse = os.fspath(brand_dir / 'discourse.svg')
  
    screenpal = os.fspath(brand_dir / 'screenpal.svg')
  
    speakap = os.fspath(brand_dir / 'speakap.svg')
  
    cotton_bureau = os.fspath(brand_dir / 'cotton-bureau.svg')
  
    skype = os.fspath(brand_dir / 'skype.svg')
  
    itunes = os.fspath(brand_dir / 'itunes.svg')
  
    accusoft = os.fspath(brand_dir / 'accusoft.svg')
  
    red_river = os.fspath(brand_dir / 'red-river.svg')
  
    square_dribbble = os.fspath(brand_dir / 'square-dribbble.svg')
  
    mdb = os.fspath(brand_dir / 'mdb.svg')
  
    wolf_pack_battalion = os.fspath(brand_dir / 'wolf-pack-battalion.svg')
  
    cc_apple_pay = os.fspath(brand_dir / 'cc-apple-pay.svg')
  
    _500px = os.fspath(brand_dir / '500px.svg')
  
    snapchat = os.fspath(brand_dir / 'snapchat.svg')
  
    simplybuilt = os.fspath(brand_dir / 'simplybuilt.svg')
  
    gg = os.fspath(brand_dir / 'gg.svg')
  
    waze = os.fspath(brand_dir / 'waze.svg')
  
    hire_a_helper = os.fspath(brand_dir / 'hire-a-helper.svg')
  
    get_pocket = os.fspath(brand_dir / 'get-pocket.svg')
  
    google_wallet = os.fspath(brand_dir / 'google-wallet.svg')
  
    figma = os.fspath(brand_dir / 'figma.svg')
  
    hips = os.fspath(brand_dir / 'hips.svg')
  
    google_plus = os.fspath(brand_dir / 'google-plus.svg')
  
    steam = os.fspath(brand_dir / 'steam.svg')
  
    sourcetree = os.fspath(brand_dir / 'sourcetree.svg')
  
    bitcoin = os.fspath(brand_dir / 'bitcoin.svg')
  
    cc_paypal = os.fspath(brand_dir / 'cc-paypal.svg')
  
    cloudscale = os.fspath(brand_dir / 'cloudscale.svg')
  
    grav = os.fspath(brand_dir / 'grav.svg')
  
    meta = os.fspath(brand_dir / 'meta.svg')
  
    cc_stripe = os.fspath(brand_dir / 'cc-stripe.svg')
  
    cuttlefish = os.fspath(brand_dir / 'cuttlefish.svg')
  
    shirtsinbulk = os.fspath(brand_dir / 'shirtsinbulk.svg')
  
    vine = os.fspath(brand_dir / 'vine.svg')
  
    draft2digital = os.fspath(brand_dir / 'draft2digital.svg')
  
    fort_awesome = os.fspath(brand_dir / 'fort-awesome.svg')
  
    flipboard = os.fspath(brand_dir / 'flipboard.svg')
  
    opera = os.fspath(brand_dir / 'opera.svg')
  
    telegram = os.fspath(brand_dir / 'telegram.svg')
  
    glide = os.fspath(brand_dir / 'glide.svg')
  
    square_lastfm = os.fspath(brand_dir / 'square-lastfm.svg')
  
    pied_piper_hat = os.fspath(brand_dir / 'pied-piper-hat.svg')
  
    wordpress_simple = os.fspath(brand_dir / 'wordpress-simple.svg')
  
    brave_reverse = os.fspath(brand_dir / 'brave-reverse.svg')
  
    cloudsmith = os.fspath(brand_dir / 'cloudsmith.svg')
  
    cc_jcb = os.fspath(brand_dir / 'cc-jcb.svg')
  
    audible = os.fspath(brand_dir / 'audible.svg')
  
    ravelry = os.fspath(brand_dir / 'ravelry.svg')
  
    napster = os.fspath(brand_dir / 'napster.svg')
  
    canadian_maple_leaf = os.fspath(brand_dir / 'canadian-maple-leaf.svg')
  
    threads = os.fspath(brand_dir / 'threads.svg')
  
    modx = os.fspath(brand_dir / 'modx.svg')
  
    vimeo = os.fspath(brand_dir / 'vimeo.svg')
  
    leanpub = os.fspath(brand_dir / 'leanpub.svg')
  
    creative_commons_sampling = os.fspath(brand_dir / 'creative-commons-sampling.svg')
  
    servicestack = os.fspath(brand_dir / 'servicestack.svg')
  
    tiktok = os.fspath(brand_dir / 'tiktok.svg')
  
    odysee = os.fspath(brand_dir / 'odysee.svg')
  
    pinterest_p = os.fspath(brand_dir / 'pinterest-p.svg')
  
    usps = os.fspath(brand_dir / 'usps.svg')
  
    stubber = os.fspath(brand_dir / 'stubber.svg')
  
    connectdevelop = os.fspath(brand_dir / 'connectdevelop.svg')
  
    php = os.fspath(brand_dir / 'php.svg')
  
    zhihu = os.fspath(brand_dir / 'zhihu.svg')
  
    codepen = os.fspath(brand_dir / 'codepen.svg')
  
    youtube = os.fspath(brand_dir / 'youtube.svg')
  
    hive = os.fspath(brand_dir / 'hive.svg')
  
    upwork = os.fspath(brand_dir / 'upwork.svg')
  
    teamspeak = os.fspath(brand_dir / 'teamspeak.svg')
  
    octopus_deploy = os.fspath(brand_dir / 'octopus-deploy.svg')
  
    pixiv = os.fspath(brand_dir / 'pixiv.svg')
  
    creative_commons_nc_eu = os.fspath(brand_dir / 'creative-commons-nc-eu.svg')
  
    sketch = os.fspath(brand_dir / 'sketch.svg')
  
    wirsindhandwerk = os.fspath(brand_dir / 'wirsindhandwerk.svg')
  
    gripfire = os.fspath(brand_dir / 'gripfire.svg')
  
    qq = os.fspath(brand_dir / 'qq.svg')
  
    java = os.fspath(brand_dir / 'java.svg')
  
    hacker_news = os.fspath(brand_dir / 'hacker-news.svg')
  
    speaker_deck = os.fspath(brand_dir / 'speaker-deck.svg')
  
    square_instagram = os.fspath(brand_dir / 'square-instagram.svg')
  
    dropbox = os.fspath(brand_dir / 'dropbox.svg')
  
    bots = os.fspath(brand_dir / 'bots.svg')
  
    app_store = os.fspath(brand_dir / 'app-store.svg')
  
    phoenix_squadron = os.fspath(brand_dir / 'phoenix-squadron.svg')
  
    square_xing = os.fspath(brand_dir / 'square-xing.svg')
  
    line = os.fspath(brand_dir / 'line.svg')
  
    gofore = os.fspath(brand_dir / 'gofore.svg')
  
    old_republic = os.fspath(brand_dir / 'old-republic.svg')
  
    ethereum = os.fspath(brand_dir / 'ethereum.svg')
  
    square_github = os.fspath(brand_dir / 'square-github.svg')
  
    square_snapchat = os.fspath(brand_dir / 'square-snapchat.svg')
  
    stack_overflow = os.fspath(brand_dir / 'stack-overflow.svg')
  
    stripe = os.fspath(brand_dir / 'stripe.svg')
  
    yelp = os.fspath(brand_dir / 'yelp.svg')
  
    css3 = os.fspath(brand_dir / 'css3.svg')
  
    guilded = os.fspath(brand_dir / 'guilded.svg')
  
    behance = os.fspath(brand_dir / 'behance.svg')
  
    gitlab = os.fspath(brand_dir / 'gitlab.svg')
  
    docker = os.fspath(brand_dir / 'docker.svg')
  
    alipay = os.fspath(brand_dir / 'alipay.svg')
  
    r_project = os.fspath(brand_dir / 'r-project.svg')
  
    stripe_s = os.fspath(brand_dir / 'stripe-s.svg')
  
    apper = os.fspath(brand_dir / 'apper.svg')
  
    rev = os.fspath(brand_dir / 'rev.svg')
  
    dashcube = os.fspath(brand_dir / 'dashcube.svg')
  
    yarn = os.fspath(brand_dir / 'yarn.svg')
  
    blogger = os.fspath(brand_dir / 'blogger.svg')
  
    deezer = os.fspath(brand_dir / 'deezer.svg')
  
    slack = os.fspath(brand_dir / 'slack.svg')
  
    discord = os.fspath(brand_dir / 'discord.svg')
  
    redhat = os.fspath(brand_dir / 'redhat.svg')
  
    rebel = os.fspath(brand_dir / 'rebel.svg')
  
    uikit = os.fspath(brand_dir / 'uikit.svg')
  
    lastfm = os.fspath(brand_dir / 'lastfm.svg')
  
    js = os.fspath(brand_dir / 'js.svg')
  
    umbraco = os.fspath(brand_dir / 'umbraco.svg')
  
    creative_commons_nc = os.fspath(brand_dir / 'creative-commons-nc.svg')
  
    letterboxd = os.fspath(brand_dir / 'letterboxd.svg')
  
    app_store_ios = os.fspath(brand_dir / 'app-store-ios.svg')
  
    phoenix_framework = os.fspath(brand_dir / 'phoenix-framework.svg')
  
    goodreads_g = os.fspath(brand_dir / 'goodreads-g.svg')
  
    nutritionix = os.fspath(brand_dir / 'nutritionix.svg')
  
    square_git = os.fspath(brand_dir / 'square-git.svg')
  
    maxcdn = os.fspath(brand_dir / 'maxcdn.svg')
  
    cpanel = os.fspath(brand_dir / 'cpanel.svg')
  
    galactic_republic = os.fspath(brand_dir / 'galactic-republic.svg')
  
    jenkins = os.fspath(brand_dir / 'jenkins.svg')
  
    elementor = os.fspath(brand_dir / 'elementor.svg')
  
    square_threads = os.fspath(brand_dir / 'square-threads.svg')
  
    the_red_yeti = os.fspath(brand_dir / 'the-red-yeti.svg')
  
    wpexplorer = os.fspath(brand_dir / 'wpexplorer.svg')
  
    yandex = os.fspath(brand_dir / 'yandex.svg')
  
    fantasy_flight_games = os.fspath(brand_dir / 'fantasy-flight-games.svg')
  
    gitkraken = os.fspath(brand_dir / 'gitkraken.svg')
  
    researchgate = os.fspath(brand_dir / 'researchgate.svg')
  
    kickstarter_k = os.fspath(brand_dir / 'kickstarter-k.svg')
  
    steam_symbol = os.fspath(brand_dir / 'steam-symbol.svg')
  
    cloudversify = os.fspath(brand_dir / 'cloudversify.svg')
  
    wix = os.fspath(brand_dir / 'wix.svg')
  
    cc_visa = os.fspath(brand_dir / 'cc-visa.svg')
  
    adversal = os.fspath(brand_dir / 'adversal.svg')
  
    google_drive = os.fspath(brand_dir / 'google-drive.svg')
  
    opensuse = os.fspath(brand_dir / 'opensuse.svg')
  
    accessible_icon = os.fspath(brand_dir / 'accessible-icon.svg')
  
    bootstrap = os.fspath(brand_dir / 'bootstrap.svg')
  
    weebly = os.fspath(brand_dir / 'weebly.svg')
  
    creative_commons_share = os.fspath(brand_dir / 'creative-commons-share.svg')
  
    odnoklassniki = os.fspath(brand_dir / 'odnoklassniki.svg')
  
    itch_io = os.fspath(brand_dir / 'itch-io.svg')
  
    amazon = os.fspath(brand_dir / 'amazon.svg')
  
    ember = os.fspath(brand_dir / 'ember.svg')
  
    empire = os.fspath(brand_dir / 'empire.svg')
  
    creative_commons_zero = os.fspath(brand_dir / 'creative-commons-zero.svg')
  
    untappd = os.fspath(brand_dir / 'untappd.svg')
  
    megaport = os.fspath(brand_dir / 'megaport.svg')
  
    joomla = os.fspath(brand_dir / 'joomla.svg')
  
    salesforce = os.fspath(brand_dir / 'salesforce.svg')
  
    git_alt = os.fspath(brand_dir / 'git-alt.svg')
  
    themeisle = os.fspath(brand_dir / 'themeisle.svg')
  
    golang = os.fspath(brand_dir / 'golang.svg')
  
    reddit = os.fspath(brand_dir / 'reddit.svg')
  
    page4 = os.fspath(brand_dir / 'page4.svg')
  
    bity = os.fspath(brand_dir / 'bity.svg')
  
    dhl = os.fspath(brand_dir / 'dhl.svg')
  
    firefox = os.fspath(brand_dir / 'firefox.svg')
  
    kaggle = os.fspath(brand_dir / 'kaggle.svg')
  
    square_font_awesome_stroke = os.fspath(brand_dir / 'square-font-awesome-stroke.svg')
  
    npm = os.fspath(brand_dir / 'npm.svg')
  
    swift = os.fspath(brand_dir / 'swift.svg')
  
    artstation = os.fspath(brand_dir / 'artstation.svg')
  
    dailymotion = os.fspath(brand_dir / 'dailymotion.svg')
  
    space_awesome = os.fspath(brand_dir / 'space-awesome.svg')
  
    expeditedssl = os.fspath(brand_dir / 'expeditedssl.svg')
  
    viber = os.fspath(brand_dir / 'viber.svg')
  


class _Regular(Enum):
  
    calendar_plus = os.fspath(regular_dir / 'calendar-plus.svg')
  
    folder = os.fspath(regular_dir / 'folder.svg')
  
    face_kiss = os.fspath(regular_dir / 'face-kiss.svg')
  
    file_video = os.fspath(regular_dir / 'file-video.svg')
  
    address_card = os.fspath(regular_dir / 'address-card.svg')
  
    id_badge = os.fspath(regular_dir / 'id-badge.svg')
  
    square_caret_left = os.fspath(regular_dir / 'square-caret-left.svg')
  
    square_plus = os.fspath(regular_dir / 'square-plus.svg')
  
    face_laugh = os.fspath(regular_dir / 'face-laugh.svg')
  
    lightbulb = os.fspath(regular_dir / 'lightbulb.svg')
  
    face_kiss_beam = os.fspath(regular_dir / 'face-kiss-beam.svg')
  
    copy = os.fspath(regular_dir / 'copy.svg')
  
    circle_check = os.fspath(regular_dir / 'circle-check.svg')
  
    square_caret_right = os.fspath(regular_dir / 'square-caret-right.svg')
  
    calendar = os.fspath(regular_dir / 'calendar.svg')
  
    envelope_open = os.fspath(regular_dir / 'envelope-open.svg')
  
    bell_slash = os.fspath(regular_dir / 'bell-slash.svg')
  
    calendar_days = os.fspath(regular_dir / 'calendar-days.svg')
  
    circle_down = os.fspath(regular_dir / 'circle-down.svg')
  
    chess_knight = os.fspath(regular_dir / 'chess-knight.svg')
  
    rectangle_xmark = os.fspath(regular_dir / 'rectangle-xmark.svg')
  
    square_check = os.fspath(regular_dir / 'square-check.svg')
  
    hand_scissors = os.fspath(regular_dir / 'hand-scissors.svg')
  
    comment_dots = os.fspath(regular_dir / 'comment-dots.svg')
  
    file_zipper = os.fspath(regular_dir / 'file-zipper.svg')
  
    face_smile_wink = os.fspath(regular_dir / 'face-smile-wink.svg')
  
    image = os.fspath(regular_dir / 'image.svg')
  
    map = os.fspath(regular_dir / 'map.svg')
  
    star_half_stroke = os.fspath(regular_dir / 'star-half-stroke.svg')
  
    rectangle_list = os.fspath(regular_dir / 'rectangle-list.svg')
  
    circle_play = os.fspath(regular_dir / 'circle-play.svg')
  
    hourglass = os.fspath(regular_dir / 'hourglass.svg')
  
    flag = os.fspath(regular_dir / 'flag.svg')
  
    face_flushed = os.fspath(regular_dir / 'face-flushed.svg')
  
    eye_slash = os.fspath(regular_dir / 'eye-slash.svg')
  
    chess_pawn = os.fspath(regular_dir / 'chess-pawn.svg')
  
    file_lines = os.fspath(regular_dir / 'file-lines.svg')
  
    comments = os.fspath(regular_dir / 'comments.svg')
  
    circle_left = os.fspath(regular_dir / 'circle-left.svg')
  
    compass = os.fspath(regular_dir / 'compass.svg')
  
    file_image = os.fspath(regular_dir / 'file-image.svg')
  
    heart = os.fspath(regular_dir / 'heart.svg')
  
    paper_plane = os.fspath(regular_dir / 'paper-plane.svg')
  
    face_grin_squint_tears = os.fspath(regular_dir / 'face-grin-squint-tears.svg')
  
    comment = os.fspath(regular_dir / 'comment.svg')
  
    clock = os.fspath(regular_dir / 'clock.svg')
  
    keyboard = os.fspath(regular_dir / 'keyboard.svg')
  
    object_group = os.fspath(regular_dir / 'object-group.svg')
  
    user = os.fspath(regular_dir / 'user.svg')
  
    face_smile_beam = os.fspath(regular_dir / 'face-smile-beam.svg')
  
    handshake = os.fspath(regular_dir / 'handshake.svg')
  
    share_from_square = os.fspath(regular_dir / 'share-from-square.svg')
  
    credit_card = os.fspath(regular_dir / 'credit-card.svg')
  
    circle_up = os.fspath(regular_dir / 'circle-up.svg')
  
    face_frown_open = os.fspath(regular_dir / 'face-frown-open.svg')
  
    file_audio = os.fspath(regular_dir / 'file-audio.svg')
  
    note_sticky = os.fspath(regular_dir / 'note-sticky.svg')
  
    face_laugh_beam = os.fspath(regular_dir / 'face-laugh-beam.svg')
  
    window_restore = os.fspath(regular_dir / 'window-restore.svg')
  
    chess_bishop = os.fspath(regular_dir / 'chess-bishop.svg')
  
    font_awesome = os.fspath(regular_dir / 'font-awesome.svg')
  
    envelope = os.fspath(regular_dir / 'envelope.svg')
  
    hand_point_right = os.fspath(regular_dir / 'hand-point-right.svg')
  
    face_kiss_wink_heart = os.fspath(regular_dir / 'face-kiss-wink-heart.svg')
  
    window_maximize = os.fspath(regular_dir / 'window-maximize.svg')
  
    face_surprise = os.fspath(regular_dir / 'face-surprise.svg')
  
    face_meh = os.fspath(regular_dir / 'face-meh.svg')
  
    circle_question = os.fspath(regular_dir / 'circle-question.svg')
  
    file_excel = os.fspath(regular_dir / 'file-excel.svg')
  
    images = os.fspath(regular_dir / 'images.svg')
  
    moon = os.fspath(regular_dir / 'moon.svg')
  
    face_grin_squint = os.fspath(regular_dir / 'face-grin-squint.svg')
  
    building = os.fspath(regular_dir / 'building.svg')
  
    clone = os.fspath(regular_dir / 'clone.svg')
  
    face_frown = os.fspath(regular_dir / 'face-frown.svg')
  
    circle_pause = os.fspath(regular_dir / 'circle-pause.svg')
  
    folder_closed = os.fspath(regular_dir / 'folder-closed.svg')
  
    sun = os.fspath(regular_dir / 'sun.svg')
  
    face_sad_cry = os.fspath(regular_dir / 'face-sad-cry.svg')
  
    hand = os.fspath(regular_dir / 'hand.svg')
  
    hand_lizard = os.fspath(regular_dir / 'hand-lizard.svg')
  
    hourglass_half = os.fspath(regular_dir / 'hourglass-half.svg')
  
    floppy_disk = os.fspath(regular_dir / 'floppy-disk.svg')
  
    registered = os.fspath(regular_dir / 'registered.svg')
  
    window_minimize = os.fspath(regular_dir / 'window-minimize.svg')
  
    file_word = os.fspath(regular_dir / 'file-word.svg')
  
    square = os.fspath(regular_dir / 'square.svg')
  
    circle_stop = os.fspath(regular_dir / 'circle-stop.svg')
  
    face_laugh_wink = os.fspath(regular_dir / 'face-laugh-wink.svg')
  
    face_smile = os.fspath(regular_dir / 'face-smile.svg')
  
    face_angry = os.fspath(regular_dir / 'face-angry.svg')
  
    copyright = os.fspath(regular_dir / 'copyright.svg')
  
    file_code = os.fspath(regular_dir / 'file-code.svg')
  
    face_laugh_squint = os.fspath(regular_dir / 'face-laugh-squint.svg')
  
    chart_bar = os.fspath(regular_dir / 'chart-bar.svg')
  
    bell = os.fspath(regular_dir / 'bell.svg')
  
    lemon = os.fspath(regular_dir / 'lemon.svg')
  
    face_sad_tear = os.fspath(regular_dir / 'face-sad-tear.svg')
  
    hand_peace = os.fspath(regular_dir / 'hand-peace.svg')
  
    chess_rook = os.fspath(regular_dir / 'chess-rook.svg')
  
    trash_can = os.fspath(regular_dir / 'trash-can.svg')
  
    face_tired = os.fspath(regular_dir / 'face-tired.svg')
  
    face_grin_hearts = os.fspath(regular_dir / 'face-grin-hearts.svg')
  
    face_grin_tongue_wink = os.fspath(regular_dir / 'face-grin-tongue-wink.svg')
  
    file_pdf = os.fspath(regular_dir / 'file-pdf.svg')
  
    chess_king = os.fspath(regular_dir / 'chess-king.svg')
  
    message = os.fspath(regular_dir / 'message.svg')
  
    futbol = os.fspath(regular_dir / 'futbol.svg')
  
    calendar_check = os.fspath(regular_dir / 'calendar-check.svg')
  
    face_meh_blank = os.fspath(regular_dir / 'face-meh-blank.svg')
  
    life_ring = os.fspath(regular_dir / 'life-ring.svg')
  
    folder_open = os.fspath(regular_dir / 'folder-open.svg')
  
    pen_to_square = os.fspath(regular_dir / 'pen-to-square.svg')
  
    square_minus = os.fspath(regular_dir / 'square-minus.svg')
  
    face_rolling_eyes = os.fspath(regular_dir / 'face-rolling-eyes.svg')
  
    file = os.fspath(regular_dir / 'file.svg')
  
    closed_captioning = os.fspath(regular_dir / 'closed-captioning.svg')
  
    hand_back_fist = os.fspath(regular_dir / 'hand-back-fist.svg')
  
    hard_drive = os.fspath(regular_dir / 'hard-drive.svg')
  
    square_caret_down = os.fspath(regular_dir / 'square-caret-down.svg')
  
    face_grin_tears = os.fspath(regular_dir / 'face-grin-tears.svg')
  
    face_grin_beam = os.fspath(regular_dir / 'face-grin-beam.svg')
  
    eye = os.fspath(regular_dir / 'eye.svg')
  
    object_ungroup = os.fspath(regular_dir / 'object-ungroup.svg')
  
    id_card = os.fspath(regular_dir / 'id-card.svg')
  
    hand_point_up = os.fspath(regular_dir / 'hand-point-up.svg')
  
    calendar_xmark = os.fspath(regular_dir / 'calendar-xmark.svg')
  
    hospital = os.fspath(regular_dir / 'hospital.svg')
  
    square_full = os.fspath(regular_dir / 'square-full.svg')
  
    star = os.fspath(regular_dir / 'star.svg')
  
    face_grimace = os.fspath(regular_dir / 'face-grimace.svg')
  
    face_grin_beam_sweat = os.fspath(regular_dir / 'face-grin-beam-sweat.svg')
  
    square_caret_up = os.fspath(regular_dir / 'square-caret-up.svg')
  
    face_dizzy = os.fspath(regular_dir / 'face-dizzy.svg')
  
    calendar_minus = os.fspath(regular_dir / 'calendar-minus.svg')
  
    face_grin_tongue_squint = os.fspath(regular_dir / 'face-grin-tongue-squint.svg')
  
    clipboard = os.fspath(regular_dir / 'clipboard.svg')
  
    face_grin_tongue = os.fspath(regular_dir / 'face-grin-tongue.svg')
  
    hand_point_left = os.fspath(regular_dir / 'hand-point-left.svg')
  
    face_grin_stars = os.fspath(regular_dir / 'face-grin-stars.svg')
  
    circle_right = os.fspath(regular_dir / 'circle-right.svg')
  
    thumbs_down = os.fspath(regular_dir / 'thumbs-down.svg')
  
    face_grin_wink = os.fspath(regular_dir / 'face-grin-wink.svg')
  
    thumbs_up = os.fspath(regular_dir / 'thumbs-up.svg')
  
    hand_point_down = os.fspath(regular_dir / 'hand-point-down.svg')
  
    star_half = os.fspath(regular_dir / 'star-half.svg')
  
    circle_xmark = os.fspath(regular_dir / 'circle-xmark.svg')
  
    chess_queen = os.fspath(regular_dir / 'chess-queen.svg')
  
    face_grin = os.fspath(regular_dir / 'face-grin.svg')
  
    hand_pointer = os.fspath(regular_dir / 'hand-pointer.svg')
  
    hand_spock = os.fspath(regular_dir / 'hand-spock.svg')
  
    file_powerpoint = os.fspath(regular_dir / 'file-powerpoint.svg')
  
    address_book = os.fspath(regular_dir / 'address-book.svg')
  
    circle_dot = os.fspath(regular_dir / 'circle-dot.svg')
  
    bookmark = os.fspath(regular_dir / 'bookmark.svg')
  
    circle_user = os.fspath(regular_dir / 'circle-user.svg')
  
    newspaper = os.fspath(regular_dir / 'newspaper.svg')
  
    circle = os.fspath(regular_dir / 'circle.svg')
  
    face_grin_wide = os.fspath(regular_dir / 'face-grin-wide.svg')
  
    snowflake = os.fspath(regular_dir / 'snowflake.svg')
  
    gem = os.fspath(regular_dir / 'gem.svg')
  
    money_bill_1 = os.fspath(regular_dir / 'money-bill-1.svg')
  
    paste = os.fspath(regular_dir / 'paste.svg')
  


class _Solid(Enum):
  
    folder_tree = os.fspath(solid_dir / 'folder-tree.svg')
  
    underline = os.fspath(solid_dir / 'underline.svg')
  
    store_slash = os.fspath(solid_dir / 'store-slash.svg')
  
    cedi_sign = os.fspath(solid_dir / 'cedi-sign.svg')
  
    a = os.fspath(solid_dir / 'a.svg')
  
    anchor_circle_xmark = os.fspath(solid_dir / 'anchor-circle-xmark.svg')
  
    phone = os.fspath(solid_dir / 'phone.svg')
  
    calendar_plus = os.fspath(solid_dir / 'calendar-plus.svg')
  
    khanda = os.fspath(solid_dir / 'khanda.svg')
  
    vest = os.fspath(solid_dir / 'vest.svg')
  
    gifts = os.fspath(solid_dir / 'gifts.svg')
  
    person_digging = os.fspath(solid_dir / 'person-digging.svg')
  
    hat_cowboy = os.fspath(solid_dir / 'hat-cowboy.svg')
  
    drum = os.fspath(solid_dir / 'drum.svg')
  
    handshake_angle = os.fspath(solid_dir / 'handshake-angle.svg')
  
    charging_station = os.fspath(solid_dir / 'charging-station.svg')
  
    virus_slash = os.fspath(solid_dir / 'virus-slash.svg')
  
    indent = os.fspath(solid_dir / 'indent.svg')
  
    transgender = os.fspath(solid_dir / 'transgender.svg')
  
    person_breastfeeding = os.fspath(solid_dir / 'person-breastfeeding.svg')
  
    drumstick_bite = os.fspath(solid_dir / 'drumstick-bite.svg')
  
    circle_minus = os.fspath(solid_dir / 'circle-minus.svg')
  
    arrow_trend_down = os.fspath(solid_dir / 'arrow-trend-down.svg')
  
    hands_holding = os.fspath(solid_dir / 'hands-holding.svg')
  
    trash = os.fspath(solid_dir / 'trash.svg')
  
    plane_up = os.fspath(solid_dir / 'plane-up.svg')
  
    person_falling = os.fspath(solid_dir / 'person-falling.svg')
  
    hospital_user = os.fspath(solid_dir / 'hospital-user.svg')
  
    mars_stroke_right = os.fspath(solid_dir / 'mars-stroke-right.svg')
  
    v = os.fspath(solid_dir / 'v.svg')
  
    file_signature = os.fspath(solid_dir / 'file-signature.svg')
  
    book_journal_whills = os.fspath(solid_dir / 'book-journal-whills.svg')
  
    peseta_sign = os.fspath(solid_dir / 'peseta-sign.svg')
  
    person_drowning = os.fspath(solid_dir / 'person-drowning.svg')
  
    menorah = os.fspath(solid_dir / 'menorah.svg')
  
    meteor = os.fspath(solid_dir / 'meteor.svg')
  
    table_cells_large = os.fspath(solid_dir / 'table-cells-large.svg')
  
    arrow_rotate_left = os.fspath(solid_dir / 'arrow-rotate-left.svg')
  
    folder = os.fspath(solid_dir / 'folder.svg')
  
    business_time = os.fspath(solid_dir / 'business-time.svg')
  
    microphone_slash = os.fspath(solid_dir / 'microphone-slash.svg')
  
    arrow_right = os.fspath(solid_dir / 'arrow-right.svg')
  
    user_astronaut = os.fspath(solid_dir / 'user-astronaut.svg')
  
    face_kiss = os.fspath(solid_dir / 'face-kiss.svg')
  
    screwdriver_wrench = os.fspath(solid_dir / 'screwdriver-wrench.svg')
  
    hashtag = os.fspath(solid_dir / 'hashtag.svg')
  
    eye_dropper = os.fspath(solid_dir / 'eye-dropper.svg')
  
    quote_right = os.fspath(solid_dir / 'quote-right.svg')
  
    share = os.fspath(solid_dir / 'share.svg')
  
    spoon = os.fspath(solid_dir / 'spoon.svg')
  
    file_video = os.fspath(solid_dir / 'file-video.svg')
  
    align_justify = os.fspath(solid_dir / 'align-justify.svg')
  
    bangladeshi_taka_sign = os.fspath(solid_dir / 'bangladeshi-taka-sign.svg')
  
    z = os.fspath(solid_dir / 'z.svg')
  
    paragraph = os.fspath(solid_dir / 'paragraph.svg')
  
    arrow_up_9_1 = os.fspath(solid_dir / 'arrow-up-9-1.svg')
  
    poo_storm = os.fspath(solid_dir / 'poo-storm.svg')
  
    van_shuttle = os.fspath(solid_dir / 'van-shuttle.svg')
  
    ferry = os.fspath(solid_dir / 'ferry.svg')
  
    microphone_lines = os.fspath(solid_dir / 'microphone-lines.svg')
  
    angles_right = os.fspath(solid_dir / 'angles-right.svg')
  
    florin_sign = os.fspath(solid_dir / 'florin-sign.svg')
  
    land_mine_on = os.fspath(solid_dir / 'land-mine-on.svg')
  
    power_off = os.fspath(solid_dir / 'power-off.svg')
  
    address_card = os.fspath(solid_dir / 'address-card.svg')
  
    filter_circle_dollar = os.fspath(solid_dir / 'filter-circle-dollar.svg')
  
    dungeon = os.fspath(solid_dir / 'dungeon.svg')
  
    book_bible = os.fspath(solid_dir / 'book-bible.svg')
  
    angle_left = os.fspath(solid_dir / 'angle-left.svg')
  
    file_shield = os.fspath(solid_dir / 'file-shield.svg')
  
    hand_holding = os.fspath(solid_dir / 'hand-holding.svg')
  
    bottle_droplet = os.fspath(solid_dir / 'bottle-droplet.svg')
  
    user_shield = os.fspath(solid_dir / 'user-shield.svg')
  
    house_circle_check = os.fspath(solid_dir / 'house-circle-check.svg')
  
    _0 = os.fspath(solid_dir / '0.svg')
  
    id_badge = os.fspath(solid_dir / 'id-badge.svg')
  
    book = os.fspath(solid_dir / 'book.svg')
  
    volume_off = os.fspath(solid_dir / 'volume-off.svg')
  
    arrow_trend_up = os.fspath(solid_dir / 'arrow-trend-up.svg')
  
    mill_sign = os.fspath(solid_dir / 'mill-sign.svg')
  
    xmarks_lines = os.fspath(solid_dir / 'xmarks-lines.svg')
  
    yin_yang = os.fspath(solid_dir / 'yin-yang.svg')
  
    square_caret_left = os.fspath(solid_dir / 'square-caret-left.svg')
  
    strikethrough = os.fspath(solid_dir / 'strikethrough.svg')
  
    suitcase_medical = os.fspath(solid_dir / 'suitcase-medical.svg')
  
    boxes_packing = os.fspath(solid_dir / 'boxes-packing.svg')
  
    fire_flame_curved = os.fspath(solid_dir / 'fire-flame-curved.svg')
  
    genderless = os.fspath(solid_dir / 'genderless.svg')
  
    wave_square = os.fspath(solid_dir / 'wave-square.svg')
  
    book_bookmark = os.fspath(solid_dir / 'book-bookmark.svg')
  
    icicles = os.fspath(solid_dir / 'icicles.svg')
  
    plane_circle_check = os.fspath(solid_dir / 'plane-circle-check.svg')
  
    square_plus = os.fspath(solid_dir / 'square-plus.svg')
  
    vihara = os.fspath(solid_dir / 'vihara.svg')
  
    vial_virus = os.fspath(solid_dir / 'vial-virus.svg')
  
    trash_can_arrow_up = os.fspath(solid_dir / 'trash-can-arrow-up.svg')
  
    italic = os.fspath(solid_dir / 'italic.svg')
  
    hourglass_start = os.fspath(solid_dir / 'hourglass-start.svg')
  
    candy_cane = os.fspath(solid_dir / 'candy-cane.svg')
  
    building_un = os.fspath(solid_dir / 'building-un.svg')
  
    wallet = os.fspath(solid_dir / 'wallet.svg')
  
    forward_step = os.fspath(solid_dir / 'forward-step.svg')
  
    person_circle_plus = os.fspath(solid_dir / 'person-circle-plus.svg')
  
    passport = os.fspath(solid_dir / 'passport.svg')
  
    person_walking = os.fspath(solid_dir / 'person-walking.svg')
  
    building_user = os.fspath(solid_dir / 'building-user.svg')
  
    heart_circle_check = os.fspath(solid_dir / 'heart-circle-check.svg')
  
    video = os.fspath(solid_dir / 'video.svg')
  
    lungs_virus = os.fspath(solid_dir / 'lungs-virus.svg')
  
    circle_chevron_up = os.fspath(solid_dir / 'circle-chevron-up.svg')
  
    book_quran = os.fspath(solid_dir / 'book-quran.svg')
  
    laptop_code = os.fspath(solid_dir / 'laptop-code.svg')
  
    microphone_lines_slash = os.fspath(solid_dir / 'microphone-lines-slash.svg')
  
    anchor_lock = os.fspath(solid_dir / 'anchor-lock.svg')
  
    disease = os.fspath(solid_dir / 'disease.svg')
  
    bahai = os.fspath(solid_dir / 'bahai.svg')
  
    euro_sign = os.fspath(solid_dir / 'euro-sign.svg')
  
    hand_sparkles = os.fspath(solid_dir / 'hand-sparkles.svg')
  
    cubes_stacked = os.fspath(solid_dir / 'cubes-stacked.svg')
  
    l = os.fspath(solid_dir / 'l.svg')
  
    universal_access = os.fspath(solid_dir / 'universal-access.svg')
  
    infinity = os.fspath(solid_dir / 'infinity.svg')
  
    face_laugh = os.fspath(solid_dir / 'face-laugh.svg')
  
    bed = os.fspath(solid_dir / 'bed.svg')
  
    square_share_nodes = os.fspath(solid_dir / 'square-share-nodes.svg')
  
    hands_praying = os.fspath(solid_dir / 'hands-praying.svg')
  
    fish = os.fspath(solid_dir / 'fish.svg')
  
    tarp = os.fspath(solid_dir / 'tarp.svg')
  
    road_spikes = os.fspath(solid_dir / 'road-spikes.svg')
  
    truck_droplet = os.fspath(solid_dir / 'truck-droplet.svg')
  
    user_large_slash = os.fspath(solid_dir / 'user-large-slash.svg')
  
    gamepad = os.fspath(solid_dir / 'gamepad.svg')
  
    lightbulb = os.fspath(solid_dir / 'lightbulb.svg')
  
    angle_down = os.fspath(solid_dir / 'angle-down.svg')
  
    fire_extinguisher = os.fspath(solid_dir / 'fire-extinguisher.svg')
  
    users_gear = os.fspath(solid_dir / 'users-gear.svg')
  
    baht_sign = os.fspath(solid_dir / 'baht-sign.svg')
  
    person_circle_xmark = os.fspath(solid_dir / 'person-circle-xmark.svg')
  
    yen_sign = os.fspath(solid_dir / 'yen-sign.svg')
  
    house_chimney_crack = os.fspath(solid_dir / 'house-chimney-crack.svg')
  
    route = os.fspath(solid_dir / 'route.svg')
  
    wheat_awn = os.fspath(solid_dir / 'wheat-awn.svg')
  
    fill_drip = os.fspath(solid_dir / 'fill-drip.svg')
  
    face_kiss_beam = os.fspath(solid_dir / 'face-kiss-beam.svg')
  
    caret_up = os.fspath(solid_dir / 'caret-up.svg')
  
    bus_simple = os.fspath(solid_dir / 'bus-simple.svg')
  
    dolly = os.fspath(solid_dir / 'dolly.svg')
  
    copy = os.fspath(solid_dir / 'copy.svg')
  
    tree_city = os.fspath(solid_dir / 'tree-city.svg')
  
    battery_empty = os.fspath(solid_dir / 'battery-empty.svg')
  
    circle_check = os.fspath(solid_dir / 'circle-check.svg')
  
    bullseye = os.fspath(solid_dir / 'bullseye.svg')
  
    square_caret_right = os.fspath(solid_dir / 'square-caret-right.svg')
  
    litecoin_sign = os.fspath(solid_dir / 'litecoin-sign.svg')
  
    calendar = os.fspath(solid_dir / 'calendar.svg')
  
    train_tram = os.fspath(solid_dir / 'train-tram.svg')
  
    person_arrow_up_from_line = os.fspath(solid_dir / 'person-arrow-up-from-line.svg')
  
    icons = os.fspath(solid_dir / 'icons.svg')
  
    chart_pie = os.fspath(solid_dir / 'chart-pie.svg')
  
    wheelchair = os.fspath(solid_dir / 'wheelchair.svg')
  
    c = os.fspath(solid_dir / 'c.svg')
  
    mars_stroke_up = os.fspath(solid_dir / 'mars-stroke-up.svg')
  
    text_height = os.fspath(solid_dir / 'text-height.svg')
  
    hanukiah = os.fspath(solid_dir / 'hanukiah.svg')
  
    subscript = os.fspath(solid_dir / 'subscript.svg')
  
    user_clock = os.fspath(solid_dir / 'user-clock.svg')
  
    bullhorn = os.fspath(solid_dir / 'bullhorn.svg')
  
    paintbrush = os.fspath(solid_dir / 'paintbrush.svg')
  
    sun_plant_wilt = os.fspath(solid_dir / 'sun-plant-wilt.svg')
  
    hat_cowboy_side = os.fspath(solid_dir / 'hat-cowboy-side.svg')
  
    school_circle_xmark = os.fspath(solid_dir / 'school-circle-xmark.svg')
  
    diamond = os.fspath(solid_dir / 'diamond.svg')
  
    piggy_bank = os.fspath(solid_dir / 'piggy-bank.svg')
  
    taxi = os.fspath(solid_dir / 'taxi.svg')
  
    virus = os.fspath(solid_dir / 'virus.svg')
  
    envelope_open = os.fspath(solid_dir / 'envelope-open.svg')
  
    vial = os.fspath(solid_dir / 'vial.svg')
  
    building_ngo = os.fspath(solid_dir / 'building-ngo.svg')
  
    binoculars = os.fspath(solid_dir / 'binoculars.svg')
  
    suitcase = os.fspath(solid_dir / 'suitcase.svg')
  
    turn_down = os.fspath(solid_dir / 'turn-down.svg')
  
    bridge_water = os.fspath(solid_dir / 'bridge-water.svg')
  
    unlock_keyhole = os.fspath(solid_dir / 'unlock-keyhole.svg')
  
    grip_vertical = os.fspath(solid_dir / 'grip-vertical.svg')
  
    hryvnia_sign = os.fspath(solid_dir / 'hryvnia-sign.svg')
  
    user_graduate = os.fspath(solid_dir / 'user-graduate.svg')
  
    flag_usa = os.fspath(solid_dir / 'flag-usa.svg')
  
    circle_plus = os.fspath(solid_dir / 'circle-plus.svg')
  
    code_pull_request = os.fspath(solid_dir / 'code-pull-request.svg')
  
    file_pen = os.fspath(solid_dir / 'file-pen.svg')
  
    pen = os.fspath(solid_dir / 'pen.svg')
  
    volume_high = os.fspath(solid_dir / 'volume-high.svg')
  
    map_pin = os.fspath(solid_dir / 'map-pin.svg')
  
    earth_americas = os.fspath(solid_dir / 'earth-americas.svg')
  
    signal = os.fspath(solid_dir / 'signal.svg')
  
    jet_fighter = os.fspath(solid_dir / 'jet-fighter.svg')
  
    mobile_retro = os.fspath(solid_dir / 'mobile-retro.svg')
  
    code_compare = os.fspath(solid_dir / 'code-compare.svg')
  
    glass_water_droplet = os.fspath(solid_dir / 'glass-water-droplet.svg')
  
    check_double = os.fspath(solid_dir / 'check-double.svg')
  
    jedi = os.fspath(solid_dir / 'jedi.svg')
  
    microchip = os.fspath(solid_dir / 'microchip.svg')
  
    baby_carriage = os.fspath(solid_dir / 'baby-carriage.svg')
  
    landmark = os.fspath(solid_dir / 'landmark.svg')
  
    chevron_down = os.fspath(solid_dir / 'chevron-down.svg')
  
    person_arrow_down_to_line = os.fspath(solid_dir / 'person-arrow-down-to-line.svg')
  
    plane_lock = os.fspath(solid_dir / 'plane-lock.svg')
  
    truck_plane = os.fspath(solid_dir / 'truck-plane.svg')
  
    sleigh = os.fspath(solid_dir / 'sleigh.svg')
  
    eraser = os.fspath(solid_dir / 'eraser.svg')
  
    users_rays = os.fspath(solid_dir / 'users-rays.svg')
  
    bell_slash = os.fspath(solid_dir / 'bell-slash.svg')
  
    bridge_circle_xmark = os.fspath(solid_dir / 'bridge-circle-xmark.svg')
  
    wheat_awn_circle_exclamation = os.fspath(solid_dir / 'wheat-awn-circle-exclamation.svg')
  
    calendar_days = os.fspath(solid_dir / 'calendar-days.svg')
  
    equals = os.fspath(solid_dir / 'equals.svg')
  
    crop_simple = os.fspath(solid_dir / 'crop-simple.svg')
  
    wine_glass = os.fspath(solid_dir / 'wine-glass.svg')
  
    person_walking_luggage = os.fspath(solid_dir / 'person-walking-luggage.svg')
  
    neuter = os.fspath(solid_dir / 'neuter.svg')
  
    circle_down = os.fspath(solid_dir / 'circle-down.svg')
  
    handshake_simple = os.fspath(solid_dir / 'handshake-simple.svg')
  
    chess_knight = os.fspath(solid_dir / 'chess-knight.svg')
  
    blog = os.fspath(solid_dir / 'blog.svg')
  
    star_of_david = os.fspath(solid_dir / 'star-of-david.svg')
  
    hurricane = os.fspath(solid_dir / 'hurricane.svg')
  
    person_through_window = os.fspath(solid_dir / 'person-through-window.svg')
  
    dog = os.fspath(solid_dir / 'dog.svg')
  
    receipt = os.fspath(solid_dir / 'receipt.svg')
  
    prescription_bottle_medical = os.fspath(solid_dir / 'prescription-bottle-medical.svg')
  
    display = os.fspath(solid_dir / 'display.svg')
  
    helicopter_symbol = os.fspath(solid_dir / 'helicopter-symbol.svg')
  
    stopwatch_20 = os.fspath(solid_dir / 'stopwatch-20.svg')
  
    road_circle_check = os.fspath(solid_dir / 'road-circle-check.svg')
  
    gauge_high = os.fspath(solid_dir / 'gauge-high.svg')
  
    person_pregnant = os.fspath(solid_dir / 'person-pregnant.svg')
  
    stairs = os.fspath(solid_dir / 'stairs.svg')
  
    biohazard = os.fspath(solid_dir / 'biohazard.svg')
  
    b = os.fspath(solid_dir / 'b.svg')
  
    clipboard_list = os.fspath(solid_dir / 'clipboard-list.svg')
  
    list = os.fspath(solid_dir / 'list.svg')
  
    camera = os.fspath(solid_dir / 'camera.svg')
  
    house = os.fspath(solid_dir / 'house.svg')
  
    minimize = os.fspath(solid_dir / 'minimize.svg')
  
    weight_hanging = os.fspath(solid_dir / 'weight-hanging.svg')
  
    download = os.fspath(solid_dir / 'download.svg')
  
    drum_steelpan = os.fspath(solid_dir / 'drum-steelpan.svg')
  
    dollar_sign = os.fspath(solid_dir / 'dollar-sign.svg')
  
    rectangle_xmark = os.fspath(solid_dir / 'rectangle-xmark.svg')
  
    arrow_up_long = os.fspath(solid_dir / 'arrow-up-long.svg')
  
    hand_middle_finger = os.fspath(solid_dir / 'hand-middle-finger.svg')
  
    square_check = os.fspath(solid_dir / 'square-check.svg')
  
    comment_slash = os.fspath(solid_dir / 'comment-slash.svg')
  
    temperature_low = os.fspath(solid_dir / 'temperature-low.svg')
  
    hot_tub_person = os.fspath(solid_dir / 'hot-tub-person.svg')
  
    arrow_up_wide_short = os.fspath(solid_dir / 'arrow-up-wide-short.svg')
  
    plus = os.fspath(solid_dir / 'plus.svg')
  
    person_circle_question = os.fspath(solid_dir / 'person-circle-question.svg')
  
    hand_scissors = os.fspath(solid_dir / 'hand-scissors.svg')
  
    comment_dots = os.fspath(solid_dir / 'comment-dots.svg')
  
    list_ul = os.fspath(solid_dir / 'list-ul.svg')
  
    file_zipper = os.fspath(solid_dir / 'file-zipper.svg')
  
    ruble_sign = os.fspath(solid_dir / 'ruble-sign.svg')
  
    key = os.fspath(solid_dir / 'key.svg')
  
    paw = os.fspath(solid_dir / 'paw.svg')
  
    vest_patches = os.fspath(solid_dir / 'vest-patches.svg')
  
    fire_burner = os.fspath(solid_dir / 'fire-burner.svg')
  
    spinner = os.fspath(solid_dir / 'spinner.svg')
  
    glasses = os.fspath(solid_dir / 'glasses.svg')
  
    comments_dollar = os.fspath(solid_dir / 'comments-dollar.svg')
  
    face_smile_wink = os.fspath(solid_dir / 'face-smile-wink.svg')
  
    droplet = os.fspath(solid_dir / 'droplet.svg')
  
    couch = os.fspath(solid_dir / 'couch.svg')
  
    dice_one = os.fspath(solid_dir / 'dice-one.svg')
  
    leaf = os.fspath(solid_dir / 'leaf.svg')
  
    image = os.fspath(solid_dir / 'image.svg')
  
    trowel_bricks = os.fspath(solid_dir / 'trowel-bricks.svg')
  
    tents = os.fspath(solid_dir / 'tents.svg')
  
    tenge_sign = os.fspath(solid_dir / 'tenge-sign.svg')
  
    map = os.fspath(solid_dir / 'map.svg')
  
    star_half_stroke = os.fspath(solid_dir / 'star-half-stroke.svg')
  
    _7 = os.fspath(solid_dir / '7.svg')
  
    shekel_sign = os.fspath(solid_dir / 'shekel-sign.svg')
  
    plant_wilt = os.fspath(solid_dir / 'plant-wilt.svg')
  
    flask = os.fspath(solid_dir / 'flask.svg')
  
    rectangle_list = os.fspath(solid_dir / 'rectangle-list.svg')
  
    grip_lines = os.fspath(solid_dir / 'grip-lines.svg')
  
    gauge_simple = os.fspath(solid_dir / 'gauge-simple.svg')
  
    arrows_up_down_left_right = os.fspath(solid_dir / 'arrows-up-down-left-right.svg')
  
    chevron_left = os.fspath(solid_dir / 'chevron-left.svg')
  
    text_slash = os.fspath(solid_dir / 'text-slash.svg')
  
    gun = os.fspath(solid_dir / 'gun.svg')
  
    circle_play = os.fspath(solid_dir / 'circle-play.svg')
  
    circle_chevron_down = os.fspath(solid_dir / 'circle-chevron-down.svg')
  
    hourglass = os.fspath(solid_dir / 'hourglass.svg')
  
    head_side_mask = os.fspath(solid_dir / 'head-side-mask.svg')
  
    flag = os.fspath(solid_dir / 'flag.svg')
  
    house_chimney_medical = os.fspath(solid_dir / 'house-chimney-medical.svg')
  
    person_rays = os.fspath(solid_dir / 'person-rays.svg')
  
    parachute_box = os.fspath(solid_dir / 'parachute-box.svg')
  
    prescription = os.fspath(solid_dir / 'prescription.svg')
  
    cloud_arrow_up = os.fspath(solid_dir / 'cloud-arrow-up.svg')
  
    gears = os.fspath(solid_dir / 'gears.svg')
  
    thermometer = os.fspath(solid_dir / 'thermometer.svg')
  
    wrench = os.fspath(solid_dir / 'wrench.svg')
  
    book_medical = os.fspath(solid_dir / 'book-medical.svg')
  
    circle_arrow_right = os.fspath(solid_dir / 'circle-arrow-right.svg')
  
    face_flushed = os.fspath(solid_dir / 'face-flushed.svg')
  
    door_open = os.fspath(solid_dir / 'door-open.svg')
  
    asterisk = os.fspath(solid_dir / 'asterisk.svg')
  
    arrow_turn_down = os.fspath(solid_dir / 'arrow-turn-down.svg')
  
    user_minus = os.fspath(solid_dir / 'user-minus.svg')
  
    superscript = os.fspath(solid_dir / 'superscript.svg')
  
    lines_leaning = os.fspath(solid_dir / 'lines-leaning.svg')
  
    file_medical = os.fspath(solid_dir / 'file-medical.svg')
  
    plane = os.fspath(solid_dir / 'plane.svg')
  
    eye_slash = os.fspath(solid_dir / 'eye-slash.svg')
  
    pencil = os.fspath(solid_dir / 'pencil.svg')
  
    chess_pawn = os.fspath(solid_dir / 'chess-pawn.svg')
  
    tower_observation = os.fspath(solid_dir / 'tower-observation.svg')
  
    file_lines = os.fspath(solid_dir / 'file-lines.svg')
  
    person_circle_minus = os.fspath(solid_dir / 'person-circle-minus.svg')
  
    comments = os.fspath(solid_dir / 'comments.svg')
  
    industry = os.fspath(solid_dir / 'industry.svg')
  
    hotel = os.fspath(solid_dir / 'hotel.svg')
  
    person_dress = os.fspath(solid_dir / 'person-dress.svg')
  
    money_bill_transfer = os.fspath(solid_dir / 'money-bill-transfer.svg')
  
    blender = os.fspath(solid_dir / 'blender.svg')
  
    person_military_pointing = os.fspath(solid_dir / 'person-military-pointing.svg')
  
    file_circle_plus = os.fspath(solid_dir / 'file-circle-plus.svg')
  
    mobile_screen = os.fspath(solid_dir / 'mobile-screen.svg')
  
    mug_saucer = os.fspath(solid_dir / 'mug-saucer.svg')
  
    house_medical_circle_xmark = os.fspath(solid_dir / 'house-medical-circle-xmark.svg')
  
    plug_circle_exclamation = os.fspath(solid_dir / 'plug-circle-exclamation.svg')
  
    table_tennis_paddle_ball = os.fspath(solid_dir / 'table-tennis-paddle-ball.svg')
  
    house_medical_flag = os.fspath(solid_dir / 'house-medical-flag.svg')
  
    store = os.fspath(solid_dir / 'store.svg')
  
    phone_volume = os.fspath(solid_dir / 'phone-volume.svg')
  
    truck_front = os.fspath(solid_dir / 'truck-front.svg')
  
    stop = os.fspath(solid_dir / 'stop.svg')
  
    circle_nodes = os.fspath(solid_dir / 'circle-nodes.svg')
  
    circle_left = os.fspath(solid_dir / 'circle-left.svg')
  
    user_tie = os.fspath(solid_dir / 'user-tie.svg')
  
    reply_all = os.fspath(solid_dir / 'reply-all.svg')
  
    diagram_project = os.fspath(solid_dir / 'diagram-project.svg')
  
    stamp = os.fspath(solid_dir / 'stamp.svg')
  
    dumpster_fire = os.fspath(solid_dir / 'dumpster-fire.svg')
  
    cart_arrow_down = os.fspath(solid_dir / 'cart-arrow-down.svg')
  
    compass = os.fspath(solid_dir / 'compass.svg')
  
    file_image = os.fspath(solid_dir / 'file-image.svg')
  
    vector_square = os.fspath(solid_dir / 'vector-square.svg')
  
    chart_column = os.fspath(solid_dir / 'chart-column.svg')
  
    burst = os.fspath(solid_dir / 'burst.svg')
  
    cloud = os.fspath(solid_dir / 'cloud.svg')
  
    kiwi_bird = os.fspath(solid_dir / 'kiwi-bird.svg')
  
    up_right_from_square = os.fspath(solid_dir / 'up-right-from-square.svg')
  
    ticket = os.fspath(solid_dir / 'ticket.svg')
  
    clipboard_user = os.fspath(solid_dir / 'clipboard-user.svg')
  
    outdent = os.fspath(solid_dir / 'outdent.svg')
  
    arrow_down_z_a = os.fspath(solid_dir / 'arrow-down-z-a.svg')
  
    arrows_to_circle = os.fspath(solid_dir / 'arrows-to-circle.svg')
  
    mercury = os.fspath(solid_dir / 'mercury.svg')
  
    guarani_sign = os.fspath(solid_dir / 'guarani-sign.svg')
  
    faucet_drip = os.fspath(solid_dir / 'faucet-drip.svg')
  
    x = os.fspath(solid_dir / 'x.svg')
  
    car_rear = os.fspath(solid_dir / 'car-rear.svg')
  
    x_ray = os.fspath(solid_dir / 'x-ray.svg')
  
    place_of_worship = os.fspath(solid_dir / 'place-of-worship.svg')
  
    heart = os.fspath(solid_dir / 'heart.svg')
  
    mars_and_venus_burst = os.fspath(solid_dir / 'mars-and-venus-burst.svg')
  
    rotate_right = os.fspath(solid_dir / 'rotate-right.svg')
  
    temperature_empty = os.fspath(solid_dir / 'temperature-empty.svg')
  
    paper_plane = os.fspath(solid_dir / 'paper-plane.svg')
  
    user_secret = os.fspath(solid_dir / 'user-secret.svg')
  
    eye_low_vision = os.fspath(solid_dir / 'eye-low-vision.svg')
  
    shapes = os.fspath(solid_dir / 'shapes.svg')
  
    helmet_un = os.fspath(solid_dir / 'helmet-un.svg')
  
    person_biking = os.fspath(solid_dir / 'person-biking.svg')
  
    car_on = os.fspath(solid_dir / 'car-on.svg')
  
    chalkboard = os.fspath(solid_dir / 'chalkboard.svg')
  
    face_grin_squint_tears = os.fspath(solid_dir / 'face-grin-squint-tears.svg')
  
    clipboard_check = os.fspath(solid_dir / 'clipboard-check.svg')
  
    person_cane = os.fspath(solid_dir / 'person-cane.svg')
  
    cheese = os.fspath(solid_dir / 'cheese.svg')
  
    temperature_quarter = os.fspath(solid_dir / 'temperature-quarter.svg')
  
    graduation_cap = os.fspath(solid_dir / 'graduation-cap.svg')
  
    left_right = os.fspath(solid_dir / 'left-right.svg')
  
    wand_sparkles = os.fspath(solid_dir / 'wand-sparkles.svg')
  
    users = os.fspath(solid_dir / 'users.svg')
  
    draw_polygon = os.fspath(solid_dir / 'draw-polygon.svg')
  
    tornado = os.fspath(solid_dir / 'tornado.svg')
  
    backward_fast = os.fspath(solid_dir / 'backward-fast.svg')
  
    toilets_portable = os.fspath(solid_dir / 'toilets-portable.svg')
  
    bars_staggered = os.fspath(solid_dir / 'bars-staggered.svg')
  
    arrow_down_a_z = os.fspath(solid_dir / 'arrow-down-a-z.svg')
  
    expand = os.fspath(solid_dir / 'expand.svg')
  
    comment = os.fspath(solid_dir / 'comment.svg')
  
    fan = os.fspath(solid_dir / 'fan.svg')
  
    hands_clapping = os.fspath(solid_dir / 'hands-clapping.svg')
  
    volume_low = os.fspath(solid_dir / 'volume-low.svg')
  
    up_right_and_down_left_from_center = os.fspath(solid_dir / 'up-right-and-down-left-from-center.svg')
  
    clock = os.fspath(solid_dir / 'clock.svg')
  
    school_flag = os.fspath(solid_dir / 'school-flag.svg')
  
    battery_half = os.fspath(solid_dir / 'battery-half.svg')
  
    scissors = os.fspath(solid_dir / 'scissors.svg')
  
    bone = os.fspath(solid_dir / 'bone.svg')
  
    radiation = os.fspath(solid_dir / 'radiation.svg')
  
    vr_cardboard = os.fspath(solid_dir / 'vr-cardboard.svg')
  
    city = os.fspath(solid_dir / 'city.svg')
  
    keyboard = os.fspath(solid_dir / 'keyboard.svg')
  
    check_to_slot = os.fspath(solid_dir / 'check-to-slot.svg')
  
    ruler = os.fspath(solid_dir / 'ruler.svg')
  
    book_skull = os.fspath(solid_dir / 'book-skull.svg')
  
    ruler_combined = os.fspath(solid_dir / 'ruler-combined.svg')
  
    tower_broadcast = os.fspath(solid_dir / 'tower-broadcast.svg')
  
    id_card_clip = os.fspath(solid_dir / 'id-card-clip.svg')
  
    truck_moving = os.fspath(solid_dir / 'truck-moving.svg')
  
    motorcycle = os.fspath(solid_dir / 'motorcycle.svg')
  
    object_group = os.fspath(solid_dir / 'object-group.svg')
  
    headset = os.fspath(solid_dir / 'headset.svg')
  
    bicycle = os.fspath(solid_dir / 'bicycle.svg')
  
    whiskey_glass = os.fspath(solid_dir / 'whiskey-glass.svg')
  
    audio_description = os.fspath(solid_dir / 'audio-description.svg')
  
    user = os.fspath(solid_dir / 'user.svg')
  
    magnet = os.fspath(solid_dir / 'magnet.svg')
  
    sink = os.fspath(solid_dir / 'sink.svg')
  
    teeth = os.fspath(solid_dir / 'teeth.svg')
  
    traffic_light = os.fspath(solid_dir / 'traffic-light.svg')
  
    face_smile_beam = os.fspath(solid_dir / 'face-smile-beam.svg')
  
    spa = os.fspath(solid_dir / 'spa.svg')
  
    bomb = os.fspath(solid_dir / 'bomb.svg')
  
    person_walking_dashed_line_arrow_right = os.fspath(solid_dir / 'person-walking-dashed-line-arrow-right.svg')
  
    handshake = os.fspath(solid_dir / 'handshake.svg')
  
    person_hiking = os.fspath(solid_dir / 'person-hiking.svg')
  
    share_from_square = os.fspath(solid_dir / 'share-from-square.svg')
  
    hand_holding_heart = os.fspath(solid_dir / 'hand-holding-heart.svg')
  
    square_h = os.fspath(solid_dir / 'square-h.svg')
  
    u = os.fspath(solid_dir / 'u.svg')
  
    hourglass_end = os.fspath(solid_dir / 'hourglass-end.svg')
  
    dice_two = os.fspath(solid_dir / 'dice-two.svg')
  
    signs_post = os.fspath(solid_dir / 'signs-post.svg')
  
    g = os.fspath(solid_dir / 'g.svg')
  
    credit_card = os.fspath(solid_dir / 'credit-card.svg')
  
    vault = os.fspath(solid_dir / 'vault.svg')
  
    jug_detergent = os.fspath(solid_dir / 'jug-detergent.svg')
  
    house_chimney_user = os.fspath(solid_dir / 'house-chimney-user.svg')
  
    paint_roller = os.fspath(solid_dir / 'paint-roller.svg')
  
    dna = os.fspath(solid_dir / 'dna.svg')
  
    circle_up = os.fspath(solid_dir / 'circle-up.svg')
  
    pizza_slice = os.fspath(solid_dir / 'pizza-slice.svg')
  
    earth_europe = os.fspath(solid_dir / 'earth-europe.svg')
  
    face_frown_open = os.fspath(solid_dir / 'face-frown-open.svg')
  
    heart_circle_bolt = os.fspath(solid_dir / 'heart-circle-bolt.svg')
  
    file_audio = os.fspath(solid_dir / 'file-audio.svg')
  
    chevron_right = os.fspath(solid_dir / 'chevron-right.svg')
  
    align_right = os.fspath(solid_dir / 'align-right.svg')
  
    sim_card = os.fspath(solid_dir / 'sim-card.svg')
  
    bridge_lock = os.fspath(solid_dir / 'bridge-lock.svg')
  
    border_none = os.fspath(solid_dir / 'border-none.svg')
  
    sailboat = os.fspath(solid_dir / 'sailboat.svg')
  
    cloud_rain = os.fspath(solid_dir / 'cloud-rain.svg')
  
    house_tsunami = os.fspath(solid_dir / 'house-tsunami.svg')
  
    code_commit = os.fspath(solid_dir / 'code-commit.svg')
  
    stapler = os.fspath(solid_dir / 'stapler.svg')
  
    pepper_hot = os.fspath(solid_dir / 'pepper-hot.svg')
  
    brain = os.fspath(solid_dir / 'brain.svg')
  
    sort_down = os.fspath(solid_dir / 'sort-down.svg')
  
    house_circle_xmark = os.fspath(solid_dir / 'house-circle-xmark.svg')
  
    file_waveform = os.fspath(solid_dir / 'file-waveform.svg')
  
    magnifying_glass_minus = os.fspath(solid_dir / 'magnifying-glass-minus.svg')
  
    wine_glass_empty = os.fspath(solid_dir / 'wine-glass-empty.svg')
  
    note_sticky = os.fspath(solid_dir / 'note-sticky.svg')
  
    face_laugh_beam = os.fspath(solid_dir / 'face-laugh-beam.svg')
  
    window_restore = os.fspath(solid_dir / 'window-restore.svg')
  
    road_circle_xmark = os.fspath(solid_dir / 'road-circle-xmark.svg')
  
    heart_circle_plus = os.fspath(solid_dir / 'heart-circle-plus.svg')
  
    headphones = os.fspath(solid_dir / 'headphones.svg')
  
    chess_bishop = os.fspath(solid_dir / 'chess-bishop.svg')
  
    handshake_slash = os.fspath(solid_dir / 'handshake-slash.svg')
  
    mobile_screen_button = os.fspath(solid_dir / 'mobile-screen-button.svg')
  
    lira_sign = os.fspath(solid_dir / 'lira-sign.svg')
  
    divide = os.fspath(solid_dir / 'divide.svg')
  
    font_awesome = os.fspath(solid_dir / 'font-awesome.svg')
  
    podcast = os.fspath(solid_dir / 'podcast.svg')
  
    mosque = os.fspath(solid_dir / 'mosque.svg')
  
    flag_checkered = os.fspath(solid_dir / 'flag-checkered.svg')
  
    comment_sms = os.fspath(solid_dir / 'comment-sms.svg')
  
    person_chalkboard = os.fspath(solid_dir / 'person-chalkboard.svg')
  
    hand_holding_medical = os.fspath(solid_dir / 'hand-holding-medical.svg')
  
    heart_circle_minus = os.fspath(solid_dir / 'heart-circle-minus.svg')
  
    code_fork = os.fspath(solid_dir / 'code-fork.svg')
  
    poop = os.fspath(solid_dir / 'poop.svg')
  
    clapperboard = os.fspath(solid_dir / 'clapperboard.svg')
  
    border_top_left = os.fspath(solid_dir / 'border-top-left.svg')
  
    music = os.fspath(solid_dir / 'music.svg')
  
    arrow_left_long = os.fspath(solid_dir / 'arrow-left-long.svg')
  
    person_burst = os.fspath(solid_dir / 'person-burst.svg')
  
    envelope = os.fspath(solid_dir / 'envelope.svg')
  
    plane_circle_exclamation = os.fspath(solid_dir / 'plane-circle-exclamation.svg')
  
    camera_retro = os.fspath(solid_dir / 'camera-retro.svg')
  
    jet_fighter_up = os.fspath(solid_dir / 'jet-fighter-up.svg')
  
    angles_up = os.fspath(solid_dir / 'angles-up.svg')
  
    align_left = os.fspath(solid_dir / 'align-left.svg')
  
    person_praying = os.fspath(solid_dir / 'person-praying.svg')
  
    football = os.fspath(solid_dir / 'football.svg')
  
    hand_fist = os.fspath(solid_dir / 'hand-fist.svg')
  
    hill_avalanche = os.fspath(solid_dir / 'hill-avalanche.svg')
  
    arrows_up_down = os.fspath(solid_dir / 'arrows-up-down.svg')
  
    arrow_right_long = os.fspath(solid_dir / 'arrow-right-long.svg')
  
    hand_point_right = os.fspath(solid_dir / 'hand-point-right.svg')
  
    face_kiss_wink_heart = os.fspath(solid_dir / 'face-kiss-wink-heart.svg')
  
    stethoscope = os.fspath(solid_dir / 'stethoscope.svg')
  
    toolbox = os.fspath(solid_dir / 'toolbox.svg')
  
    screwdriver = os.fspath(solid_dir / 'screwdriver.svg')
  
    car_battery = os.fspath(solid_dir / 'car-battery.svg')
  
    ship = os.fspath(solid_dir / 'ship.svg')
  
    location_pin = os.fspath(solid_dir / 'location-pin.svg')
  
    chair = os.fspath(solid_dir / 'chair.svg')
  
    arrows_up_to_line = os.fspath(solid_dir / 'arrows-up-to-line.svg')
  
    magnifying_glass = os.fspath(solid_dir / 'magnifying-glass.svg')
  
    guitar = os.fspath(solid_dir / 'guitar.svg')
  
    volcano = os.fspath(solid_dir / 'volcano.svg')
  
    window_maximize = os.fspath(solid_dir / 'window-maximize.svg')
  
    book_open_reader = os.fspath(solid_dir / 'book-open-reader.svg')
  
    hotdog = os.fspath(solid_dir / 'hotdog.svg')
  
    turkish_lira_sign = os.fspath(solid_dir / 'turkish-lira-sign.svg')
  
    arrow_up_right_dots = os.fspath(solid_dir / 'arrow-up-right-dots.svg')
  
    align_center = os.fspath(solid_dir / 'align-center.svg')
  
    face_surprise = os.fspath(solid_dir / 'face-surprise.svg')
  
    vial_circle_check = os.fspath(solid_dir / 'vial-circle-check.svg')
  
    face_meh = os.fspath(solid_dir / 'face-meh.svg')
  
    person_rifle = os.fspath(solid_dir / 'person-rifle.svg')
  
    circle_question = os.fspath(solid_dir / 'circle-question.svg')
  
    cart_flatbed_suitcase = os.fspath(solid_dir / 'cart-flatbed-suitcase.svg')
  
    down_left_and_up_right_to_center = os.fspath(solid_dir / 'down-left-and-up-right-to-center.svg')
  
    boxes_stacked = os.fspath(solid_dir / 'boxes-stacked.svg')
  
    file_excel = os.fspath(solid_dir / 'file-excel.svg')
  
    hands_bound = os.fspath(solid_dir / 'hands-bound.svg')
  
    person_circle_exclamation = os.fspath(solid_dir / 'person-circle-exclamation.svg')
  
    microphone = os.fspath(solid_dir / 'microphone.svg')
  
    cow = os.fspath(solid_dir / 'cow.svg')
  
    mountain = os.fspath(solid_dir / 'mountain.svg')
  
    repeat = os.fspath(solid_dir / 'repeat.svg')
  
    mars = os.fspath(solid_dir / 'mars.svg')
  
    hill_rockslide = os.fspath(solid_dir / 'hill-rockslide.svg')
  
    truck_medical = os.fspath(solid_dir / 'truck-medical.svg')
  
    square_xmark = os.fspath(solid_dir / 'square-xmark.svg')
  
    feather = os.fspath(solid_dir / 'feather.svg')
  
    water_ladder = os.fspath(solid_dir / 'water-ladder.svg')
  
    school = os.fspath(solid_dir / 'school.svg')
  
    images = os.fspath(solid_dir / 'images.svg')
  
    shield_cat = os.fspath(solid_dir / 'shield-cat.svg')
  
    xmark = os.fspath(solid_dir / 'xmark.svg')
  
    less_than_equal = os.fspath(solid_dir / 'less-than-equal.svg')
  
    person_skiing = os.fspath(solid_dir / 'person-skiing.svg')
  
    s = os.fspath(solid_dir / 's.svg')
  
    circle_chevron_left = os.fspath(solid_dir / 'circle-chevron-left.svg')
  
    moon = os.fspath(solid_dir / 'moon.svg')
  
    square_person_confined = os.fspath(solid_dir / 'square-person-confined.svg')
  
    earth_oceania = os.fspath(solid_dir / 'earth-oceania.svg')
  
    gauge = os.fspath(solid_dir / 'gauge.svg')
  
    triangle_exclamation = os.fspath(solid_dir / 'triangle-exclamation.svg')
  
    golf_ball_tee = os.fspath(solid_dir / 'golf-ball-tee.svg')
  
    fire_flame_simple = os.fspath(solid_dir / 'fire-flame-simple.svg')
  
    face_grin_squint = os.fspath(solid_dir / 'face-grin-squint.svg')
  
    child_reaching = os.fspath(solid_dir / 'child-reaching.svg')
  
    mosquito = os.fspath(solid_dir / 'mosquito.svg')
  
    restroom = os.fspath(solid_dir / 'restroom.svg')
  
    building = os.fspath(solid_dir / 'building.svg')
  
    _8 = os.fspath(solid_dir / '8.svg')
  
    hand_dots = os.fspath(solid_dir / 'hand-dots.svg')
  
    road_barrier = os.fspath(solid_dir / 'road-barrier.svg')
  
    user_pen = os.fspath(solid_dir / 'user-pen.svg')
  
    radio = os.fspath(solid_dir / 'radio.svg')
  
    book_tanakh = os.fspath(solid_dir / 'book-tanakh.svg')
  
    arrow_down_short_wide = os.fspath(solid_dir / 'arrow-down-short-wide.svg')
  
    indian_rupee_sign = os.fspath(solid_dir / 'indian-rupee-sign.svg')
  
    clone = os.fspath(solid_dir / 'clone.svg')
  
    heart_circle_xmark = os.fspath(solid_dir / 'heart-circle-xmark.svg')
  
    mitten = os.fspath(solid_dir / 'mitten.svg')
  
    arrows_turn_right = os.fspath(solid_dir / 'arrows-turn-right.svg')
  
    file_csv = os.fspath(solid_dir / 'file-csv.svg')
  
    ankh = os.fspath(solid_dir / 'ankh.svg')
  
    crown = os.fspath(solid_dir / 'crown.svg')
  
    scroll_torah = os.fspath(solid_dir / 'scroll-torah.svg')
  
    arrow_down_9_1 = os.fspath(solid_dir / 'arrow-down-9-1.svg')
  
    jar_wheat = os.fspath(solid_dir / 'jar-wheat.svg')
  
    mound = os.fspath(solid_dir / 'mound.svg')
  
    people_group = os.fspath(solid_dir / 'people-group.svg')
  
    truck_field = os.fspath(solid_dir / 'truck-field.svg')
  
    circle_chevron_right = os.fspath(solid_dir / 'circle-chevron-right.svg')
  
    blender_phone = os.fspath(solid_dir / 'blender-phone.svg')
  
    bottle_water = os.fspath(solid_dir / 'bottle-water.svg')
  
    cash_register = os.fspath(solid_dir / 'cash-register.svg')
  
    money_bills = os.fspath(solid_dir / 'money-bills.svg')
  
    money_check = os.fspath(solid_dir / 'money-check.svg')
  
    cookie_bite = os.fspath(solid_dir / 'cookie-bite.svg')
  
    user_tag = os.fspath(solid_dir / 'user-tag.svg')
  
    face_frown = os.fspath(solid_dir / 'face-frown.svg')
  
    baby = os.fspath(solid_dir / 'baby.svg')
  
    bong = os.fspath(solid_dir / 'bong.svg')
  
    plane_slash = os.fspath(solid_dir / 'plane-slash.svg')
  
    mask_ventilator = os.fspath(solid_dir / 'mask-ventilator.svg')
  
    tree = os.fspath(solid_dir / 'tree.svg')
  
    seedling = os.fspath(solid_dir / 'seedling.svg')
  
    tent = os.fspath(solid_dir / 'tent.svg')
  
    circle_pause = os.fspath(solid_dir / 'circle-pause.svg')
  
    tachograph_digital = os.fspath(solid_dir / 'tachograph-digital.svg')
  
    tablets = os.fspath(solid_dir / 'tablets.svg')
  
    folder_closed = os.fspath(solid_dir / 'folder-closed.svg')
  
    sun = os.fspath(solid_dir / 'sun.svg')
  
    face_sad_cry = os.fspath(solid_dir / 'face-sad-cry.svg')
  
    cat = os.fspath(solid_dir / 'cat.svg')
  
    dice_d6 = os.fspath(solid_dir / 'dice-d6.svg')
  
    magnifying_glass_chart = os.fspath(solid_dir / 'magnifying-glass-chart.svg')
  
    y = os.fspath(solid_dir / 'y.svg')
  
    hand = os.fspath(solid_dir / 'hand.svg')
  
    hands = os.fspath(solid_dir / 'hands.svg')
  
    bed_pulse = os.fspath(solid_dir / 'bed-pulse.svg')
  
    location_arrow = os.fspath(solid_dir / 'location-arrow.svg')
  
    building_circle_xmark = os.fspath(solid_dir / 'building-circle-xmark.svg')
  
    hand_lizard = os.fspath(solid_dir / 'hand-lizard.svg')
  
    dice_d20 = os.fspath(solid_dir / 'dice-d20.svg')
  
    tent_arrow_left_right = os.fspath(solid_dir / 'tent-arrow-left-right.svg')
  
    box_archive = os.fspath(solid_dir / 'box-archive.svg')
  
    share_nodes = os.fspath(solid_dir / 'share-nodes.svg')
  
    landmark_dome = os.fspath(solid_dir / 'landmark-dome.svg')
  
    table_cells = os.fspath(solid_dir / 'table-cells.svg')
  
    cloud_showers_water = os.fspath(solid_dir / 'cloud-showers-water.svg')
  
    kaaba = os.fspath(solid_dir / 'kaaba.svg')
  
    rss = os.fspath(solid_dir / 'rss.svg')
  
    book_open = os.fspath(solid_dir / 'book-open.svg')
  
    file_circle_minus = os.fspath(solid_dir / 'file-circle-minus.svg')
  
    ruler_horizontal = os.fspath(solid_dir / 'ruler-horizontal.svg')
  
    plug_circle_bolt = os.fspath(solid_dir / 'plug-circle-bolt.svg')
  
    toggle_on = os.fspath(solid_dir / 'toggle-on.svg')
  
    handshake_simple_slash = os.fspath(solid_dir / 'handshake-simple-slash.svg')
  
    synagogue = os.fspath(solid_dir / 'synagogue.svg')
  
    hourglass_half = os.fspath(solid_dir / 'hourglass-half.svg')
  
    street_view = os.fspath(solid_dir / 'street-view.svg')
  
    computer_mouse = os.fspath(solid_dir / 'computer-mouse.svg')
  
    marker = os.fspath(solid_dir / 'marker.svg')
  
    briefcase = os.fspath(solid_dir / 'briefcase.svg')
  
    filter = os.fspath(solid_dir / 'filter.svg')
  
    language = os.fspath(solid_dir / 'language.svg')
  
    floppy_disk = os.fspath(solid_dir / 'floppy-disk.svg')
  
    volume_xmark = os.fspath(solid_dir / 'volume-xmark.svg')
  
    calendar_week = os.fspath(solid_dir / 'calendar-week.svg')
  
    inbox = os.fspath(solid_dir / 'inbox.svg')
  
    delete_left = os.fspath(solid_dir / 'delete-left.svg')
  
    champagne_glasses = os.fspath(solid_dir / 'champagne-glasses.svg')
  
    dong_sign = os.fspath(solid_dir / 'dong-sign.svg')
  
    anchor_circle_exclamation = os.fspath(solid_dir / 'anchor-circle-exclamation.svg')
  
    tape = os.fspath(solid_dir / 'tape.svg')
  
    hands_asl_interpreting = os.fspath(solid_dir / 'hands-asl-interpreting.svg')
  
    robot = os.fspath(solid_dir / 'robot.svg')
  
    ear_listen = os.fspath(solid_dir / 'ear-listen.svg')
  
    o = os.fspath(solid_dir / 'o.svg')
  
    apple_whole = os.fspath(solid_dir / 'apple-whole.svg')
  
    up_down = os.fspath(solid_dir / 'up-down.svg')
  
    group_arrows_rotate = os.fspath(solid_dir / 'group-arrows-rotate.svg')
  
    compass_drafting = os.fspath(solid_dir / 'compass-drafting.svg')
  
    warehouse = os.fspath(solid_dir / 'warehouse.svg')
  
    notdef = os.fspath(solid_dir / 'notdef.svg')
  
    circle_arrow_up = os.fspath(solid_dir / 'circle-arrow-up.svg')
  
    bowl_food = os.fspath(solid_dir / 'bowl-food.svg')
  
    print = os.fspath(solid_dir / 'print.svg')
  
    cloud_sun = os.fspath(solid_dir / 'cloud-sun.svg')
  
    money_bill = os.fspath(solid_dir / 'money-bill.svg')
  
    arrow_right_to_city = os.fspath(solid_dir / 'arrow-right-to-city.svg')
  
    mobile_button = os.fspath(solid_dir / 'mobile-button.svg')
  
    registered = os.fspath(solid_dir / 'registered.svg')
  
    person_swimming = os.fspath(solid_dir / 'person-swimming.svg')
  
    dumbbell = os.fspath(solid_dir / 'dumbbell.svg')
  
    money_bill_wheat = os.fspath(solid_dir / 'money-bill-wheat.svg')
  
    syringe = os.fspath(solid_dir / 'syringe.svg')
  
    crutch = os.fspath(solid_dir / 'crutch.svg')
  
    jar = os.fspath(solid_dir / 'jar.svg')
  
    briefcase_medical = os.fspath(solid_dir / 'briefcase-medical.svg')
  
    tent_arrow_turn_left = os.fspath(solid_dir / 'tent-arrow-turn-left.svg')
  
    house_medical_circle_check = os.fspath(solid_dir / 'house-medical-circle-check.svg')
  
    scale_unbalanced_flip = os.fspath(solid_dir / 'scale-unbalanced-flip.svg')
  
    spray_can = os.fspath(solid_dir / 'spray-can.svg')
  
    truck_ramp_box = os.fspath(solid_dir / 'truck-ramp-box.svg')
  
    file_prescription = os.fspath(solid_dir / 'file-prescription.svg')
  
    j = os.fspath(solid_dir / 'j.svg')
  
    maximize = os.fspath(solid_dir / 'maximize.svg')
  
    frog = os.fspath(solid_dir / 'frog.svg')
  
    _1 = os.fspath(solid_dir / '1.svg')
  
    window_minimize = os.fspath(solid_dir / 'window-minimize.svg')
  
    truck_field_un = os.fspath(solid_dir / 'truck-field-un.svg')
  
    house_medical = os.fspath(solid_dir / 'house-medical.svg')
  
    ear_deaf = os.fspath(solid_dir / 'ear-deaf.svg')
  
    chart_simple = os.fspath(solid_dir / 'chart-simple.svg')
  
    code_branch = os.fspath(solid_dir / 'code-branch.svg')
  
    r = os.fspath(solid_dir / 'r.svg')
  
    table_list = os.fspath(solid_dir / 'table-list.svg')
  
    dharmachakra = os.fspath(solid_dir / 'dharmachakra.svg')
  
    bowl_rice = os.fspath(solid_dir / 'bowl-rice.svg')
  
    microscope = os.fspath(solid_dir / 'microscope.svg')
  
    dumpster = os.fspath(solid_dir / 'dumpster.svg')
  
    text_width = os.fspath(solid_dir / 'text-width.svg')
  
    capsules = os.fspath(solid_dir / 'capsules.svg')
  
    bridge = os.fspath(solid_dir / 'bridge.svg')
  
    user_lock = os.fspath(solid_dir / 'user-lock.svg')
  
    cannabis = os.fspath(solid_dir / 'cannabis.svg')
  
    chess_board = os.fspath(solid_dir / 'chess-board.svg')
  
    snowplow = os.fspath(solid_dir / 'snowplow.svg')
  
    rotate_left = os.fspath(solid_dir / 'rotate-left.svg')
  
    road_bridge = os.fspath(solid_dir / 'road-bridge.svg')
  
    arrow_up_from_ground_water = os.fspath(solid_dir / 'arrow-up-from-ground-water.svg')
  
    file_word = os.fspath(solid_dir / 'file-word.svg')
  
    square = os.fspath(solid_dir / 'square.svg')
  
    network_wired = os.fspath(solid_dir / 'network-wired.svg')
  
    elevator = os.fspath(solid_dir / 'elevator.svg')
  
    gopuram = os.fspath(solid_dir / 'gopuram.svg')
  
    _6 = os.fspath(solid_dir / '6.svg')
  
    down_long = os.fspath(solid_dir / 'down-long.svg')
  
    circle_stop = os.fspath(solid_dir / 'circle-stop.svg')
  
    file_arrow_down = os.fspath(solid_dir / 'file-arrow-down.svg')
  
    fire = os.fspath(solid_dir / 'fire.svg')
  
    gavel = os.fspath(solid_dir / 'gavel.svg')
  
    file_contract = os.fspath(solid_dir / 'file-contract.svg')
  
    bacterium = os.fspath(solid_dir / 'bacterium.svg')
  
    location_crosshairs = os.fspath(solid_dir / 'location-crosshairs.svg')
  
    face_laugh_wink = os.fspath(solid_dir / 'face-laugh-wink.svg')
  
    face_smile = os.fspath(solid_dir / 'face-smile.svg')
  
    hockey_puck = os.fspath(solid_dir / 'hockey-puck.svg')
  
    play = os.fspath(solid_dir / 'play.svg')
  
    square_phone = os.fspath(solid_dir / 'square-phone.svg')
  
    mars_stroke = os.fspath(solid_dir / 'mars-stroke.svg')
  
    gauge_simple_high = os.fspath(solid_dir / 'gauge-simple-high.svg')
  
    fingerprint = os.fspath(solid_dir / 'fingerprint.svg')
  
    memory = os.fspath(solid_dir / 'memory.svg')
  
    diagram_next = os.fspath(solid_dir / 'diagram-next.svg')
  
    house_chimney = os.fspath(solid_dir / 'house-chimney.svg')
  
    smoking = os.fspath(solid_dir / 'smoking.svg')
  
    less_than = os.fspath(solid_dir / 'less-than.svg')
  
    book_atlas = os.fspath(solid_dir / 'book-atlas.svg')
  
    voicemail = os.fspath(solid_dir / 'voicemail.svg')
  
    tooth = os.fspath(solid_dir / 'tooth.svg')
  
    bread_slice = os.fspath(solid_dir / 'bread-slice.svg')
  
    grip = os.fspath(solid_dir / 'grip.svg')
  
    plus_minus = os.fspath(solid_dir / 'plus-minus.svg')
  
    house_user = os.fspath(solid_dir / 'house-user.svg')
  
    cake_candles = os.fspath(solid_dir / 'cake-candles.svg')
  
    people_pulling = os.fspath(solid_dir / 'people-pulling.svg')
  
    shield_dog = os.fspath(solid_dir / 'shield-dog.svg')
  
    dice_four = os.fspath(solid_dir / 'dice-four.svg')
  
    not_equal = os.fspath(solid_dir / 'not-equal.svg')
  
    arrows_to_dot = os.fspath(solid_dir / 'arrows-to-dot.svg')
  
    comment_medical = os.fspath(solid_dir / 'comment-medical.svg')
  
    bandage = os.fspath(solid_dir / 'bandage.svg')
  
    feather_pointed = os.fspath(solid_dir / 'feather-pointed.svg')
  
    swatchbook = os.fspath(solid_dir / 'swatchbook.svg')
  
    mask = os.fspath(solid_dir / 'mask.svg')
  
    joint = os.fspath(solid_dir / 'joint.svg')
  
    tractor = os.fspath(solid_dir / 'tractor.svg')
  
    battery_three_quarters = os.fspath(solid_dir / 'battery-three-quarters.svg')
  
    prescription_bottle = os.fspath(solid_dir / 'prescription-bottle.svg')
  
    arrow_down_1_9 = os.fspath(solid_dir / 'arrow-down-1-9.svg')
  
    baseball = os.fspath(solid_dir / 'baseball.svg')
  
    face_angry = os.fspath(solid_dir / 'face-angry.svg')
  
    hands_holding_child = os.fspath(solid_dir / 'hands-holding-child.svg')
  
    horse_head = os.fspath(solid_dir / 'horse-head.svg')
  
    envelopes_bulk = os.fspath(solid_dir / 'envelopes-bulk.svg')
  
    franc_sign = os.fspath(solid_dir / 'franc-sign.svg')
  
    copyright = os.fspath(solid_dir / 'copyright.svg')
  
    venus_double = os.fspath(solid_dir / 'venus-double.svg')
  
    water = os.fspath(solid_dir / 'water.svg')
  
    ban = os.fspath(solid_dir / 'ban.svg')
  
    bacon = os.fspath(solid_dir / 'bacon.svg')
  
    ban_smoking = os.fspath(solid_dir / 'ban-smoking.svg')
  
    file_code = os.fspath(solid_dir / 'file-code.svg')
  
    face_laugh_squint = os.fspath(solid_dir / 'face-laugh-squint.svg')
  
    map_location_dot = os.fspath(solid_dir / 'map-location-dot.svg')
  
    compact_disc = os.fspath(solid_dir / 'compact-disc.svg')
  
    dice_five = os.fspath(solid_dir / 'dice-five.svg')
  
    pen_ruler = os.fspath(solid_dir / 'pen-ruler.svg')
  
    holly_berry = os.fspath(solid_dir / 'holly-berry.svg')
  
    mountain_sun = os.fspath(solid_dir / 'mountain-sun.svg')
  
    chart_bar = os.fspath(solid_dir / 'chart-bar.svg')
  
    bell = os.fspath(solid_dir / 'bell.svg')
  
    building_circle_exclamation = os.fspath(solid_dir / 'building-circle-exclamation.svg')
  
    lemon = os.fspath(solid_dir / 'lemon.svg')
  
    upload = os.fspath(solid_dir / 'upload.svg')
  
    wand_magic = os.fspath(solid_dir / 'wand-magic.svg')
  
    filter_circle_xmark = os.fspath(solid_dir / 'filter-circle-xmark.svg')
  
    landmark_flag = os.fspath(solid_dir / 'landmark-flag.svg')
  
    heart_pulse = os.fspath(solid_dir / 'heart-pulse.svg')
  
    database = os.fspath(solid_dir / 'database.svg')
  
    sign_hanging = os.fspath(solid_dir / 'sign-hanging.svg')
  
    face_sad_tear = os.fspath(solid_dir / 'face-sad-tear.svg')
  
    arrows_left_right_to_line = os.fspath(solid_dir / 'arrows-left-right-to-line.svg')
  
    folder_plus = os.fspath(solid_dir / 'folder-plus.svg')
  
    person_dots_from_line = os.fspath(solid_dir / 'person-dots-from-line.svg')
  
    building_columns = os.fspath(solid_dir / 'building-columns.svg')
  
    question = os.fspath(solid_dir / 'question.svg')
  
    border_all = os.fspath(solid_dir / 'border-all.svg')
  
    k = os.fspath(solid_dir / 'k.svg')
  
    oil_can = os.fspath(solid_dir / 'oil-can.svg')
  
    medal = os.fspath(solid_dir / 'medal.svg')
  
    hand_peace = os.fspath(solid_dir / 'hand-peace.svg')
  
    people_robbery = os.fspath(solid_dir / 'people-robbery.svg')
  
    dragon = os.fspath(solid_dir / 'dragon.svg')
  
    photo_film = os.fspath(solid_dir / 'photo-film.svg')
  
    star_and_crescent = os.fspath(solid_dir / 'star-and-crescent.svg')
  
    square_poll_vertical = os.fspath(solid_dir / 'square-poll-vertical.svg')
  
    spray_can_sparkles = os.fspath(solid_dir / 'spray-can-sparkles.svg')
  
    chess_rook = os.fspath(solid_dir / 'chess-rook.svg')
  
    grip_lines_vertical = os.fspath(solid_dir / 'grip-lines-vertical.svg')
  
    om = os.fspath(solid_dir / 'om.svg')
  
    trash_can = os.fspath(solid_dir / 'trash-can.svg')
  
    face_tired = os.fspath(solid_dir / 'face-tired.svg')
  
    user_doctor = os.fspath(solid_dir / 'user-doctor.svg')
  
    naira_sign = os.fspath(solid_dir / 'naira-sign.svg')
  
    cubes = os.fspath(solid_dir / 'cubes.svg')
  
    face_grin_hearts = os.fspath(solid_dir / 'face-grin-hearts.svg')
  
    face_grin_tongue_wink = os.fspath(solid_dir / 'face-grin-tongue-wink.svg')
  
    reply = os.fspath(solid_dir / 'reply.svg')
  
    file_pdf = os.fspath(solid_dir / 'file-pdf.svg')
  
    campground = os.fspath(solid_dir / 'campground.svg')
  
    toilet = os.fspath(solid_dir / 'toilet.svg')
  
    chess_king = os.fspath(solid_dir / 'chess-king.svg')
  
    caret_down = os.fspath(solid_dir / 'caret-down.svg')
  
    satellite = os.fspath(solid_dir / 'satellite.svg')
  
    font = os.fspath(solid_dir / 'font.svg')
  
    manat_sign = os.fspath(solid_dir / 'manat-sign.svg')
  
    house_flood_water = os.fspath(solid_dir / 'house-flood-water.svg')
  
    walkie_talkie = os.fspath(solid_dir / 'walkie-talkie.svg')
  
    plug_circle_minus = os.fspath(solid_dir / 'plug-circle-minus.svg')
  
    file_arrow_up = os.fspath(solid_dir / 'file-arrow-up.svg')
  
    train = os.fspath(solid_dir / 'train.svg')
  
    ethernet = os.fspath(solid_dir / 'ethernet.svg')
  
    stopwatch = os.fspath(solid_dir / 'stopwatch.svg')
  
    sd_card = os.fspath(solid_dir / 'sd-card.svg')
  
    shop_lock = os.fspath(solid_dir / 'shop-lock.svg')
  
    message = os.fspath(solid_dir / 'message.svg')
  
    magnifying_glass_location = os.fspath(solid_dir / 'magnifying-glass-location.svg')
  
    mask_face = os.fspath(solid_dir / 'mask-face.svg')
  
    person_booth = os.fspath(solid_dir / 'person-booth.svg')
  
    heart_circle_exclamation = os.fspath(solid_dir / 'heart-circle-exclamation.svg')
  
    caret_right = os.fspath(solid_dir / 'caret-right.svg')
  
    horse = os.fspath(solid_dir / 'horse.svg')
  
    heart_crack = os.fspath(solid_dir / 'heart-crack.svg')
  
    futbol = os.fspath(solid_dir / 'futbol.svg')
  
    mountain_city = os.fspath(solid_dir / 'mountain-city.svg')
  
    retweet = os.fspath(solid_dir / 'retweet.svg')
  
    house_crack = os.fspath(solid_dir / 'house-crack.svg')
  
    mug_hot = os.fspath(solid_dir / 'mug-hot.svg')
  
    tv = os.fspath(solid_dir / 'tv.svg')
  
    laptop = os.fspath(solid_dir / 'laptop.svg')
  
    baseball_bat_ball = os.fspath(solid_dir / 'baseball-bat-ball.svg')
  
    calendar_check = os.fspath(solid_dir / 'calendar-check.svg')
  
    ring = os.fspath(solid_dir / 'ring.svg')
  
    user_gear = os.fspath(solid_dir / 'user-gear.svg')
  
    temperature_arrow_up = os.fspath(solid_dir / 'temperature-arrow-up.svg')
  
    brazilian_real_sign = os.fspath(solid_dir / 'brazilian-real-sign.svg')
  
    temperature_high = os.fspath(solid_dir / 'temperature-high.svg')
  
    arrow_right_arrow_left = os.fspath(solid_dir / 'arrow-right-arrow-left.svg')
  
    face_meh_blank = os.fspath(solid_dir / 'face-meh-blank.svg')
  
    cloud_moon = os.fspath(solid_dir / 'cloud-moon.svg')
  
    kip_sign = os.fspath(solid_dir / 'kip-sign.svg')
  
    rocket = os.fspath(solid_dir / 'rocket.svg')
  
    person_walking_arrow_loop_left = os.fspath(solid_dir / 'person-walking-arrow-loop-left.svg')
  
    rotate = os.fspath(solid_dir / 'rotate.svg')
  
    trowel = os.fspath(solid_dir / 'trowel.svg')
  
    user_ninja = os.fspath(solid_dir / 'user-ninja.svg')
  
    wine_bottle = os.fspath(solid_dir / 'wine-bottle.svg')
  
    person_military_to_person = os.fspath(solid_dir / 'person-military-to-person.svg')
  
    life_ring = os.fspath(solid_dir / 'life-ring.svg')
  
    envelope_circle_check = os.fspath(solid_dir / 'envelope-circle-check.svg')
  
    recycle = os.fspath(solid_dir / 'recycle.svg')
  
    bezier_curve = os.fspath(solid_dir / 'bezier-curve.svg')
  
    shield_halved = os.fspath(solid_dir / 'shield-halved.svg')
  
    broom = os.fspath(solid_dir / 'broom.svg')
  
    quote_left = os.fspath(solid_dir / 'quote-left.svg')
  
    house_fire = os.fspath(solid_dir / 'house-fire.svg')
  
    truck_monster = os.fspath(solid_dir / 'truck-monster.svg')
  
    map_location = os.fspath(solid_dir / 'map-location.svg')
  
    angles_left = os.fspath(solid_dir / 'angles-left.svg')
  
    dice_six = os.fspath(solid_dir / 'dice-six.svg')
  
    info = os.fspath(solid_dir / 'info.svg')
  
    i = os.fspath(solid_dir / 'i.svg')
  
    bugs = os.fspath(solid_dir / 'bugs.svg')
  
    shrimp = os.fspath(solid_dir / 'shrimp.svg')
  
    faucet = os.fspath(solid_dir / 'faucet.svg')
  
    hands_holding_circle = os.fspath(solid_dir / 'hands-holding-circle.svg')
  
    video_slash = os.fspath(solid_dir / 'video-slash.svg')
  
    car_tunnel = os.fspath(solid_dir / 'car-tunnel.svg')
  
    plate_wheat = os.fspath(solid_dir / 'plate-wheat.svg')
  
    left_long = os.fspath(solid_dir / 'left-long.svg')
  
    pager = os.fspath(solid_dir / 'pager.svg')
  
    carrot = os.fspath(solid_dir / 'carrot.svg')
  
    folder_open = os.fspath(solid_dir / 'folder-open.svg')
  
    person_skiing_nordic = os.fspath(solid_dir / 'person-skiing-nordic.svg')
  
    shop_slash = os.fspath(solid_dir / 'shop-slash.svg')
  
    sterling_sign = os.fspath(solid_dir / 'sterling-sign.svg')
  
    box_open = os.fspath(solid_dir / 'box-open.svg')
  
    pen_to_square = os.fspath(solid_dir / 'pen-to-square.svg')
  
    m = os.fspath(solid_dir / 'm.svg')
  
    check = os.fspath(solid_dir / 'check.svg')
  
    square_nfi = os.fspath(solid_dir / 'square-nfi.svg')
  
    tarp_droplet = os.fspath(solid_dir / 'tarp-droplet.svg')
  
    arrow_down_wide_short = os.fspath(solid_dir / 'arrow-down-wide-short.svg')
  
    square_minus = os.fspath(solid_dir / 'square-minus.svg')
  
    arrows_spin = os.fspath(solid_dir / 'arrows-spin.svg')
  
    cable_car = os.fspath(solid_dir / 'cable-car.svg')
  
    house_laptop = os.fspath(solid_dir / 'house-laptop.svg')
  
    house_circle_exclamation = os.fspath(solid_dir / 'house-circle-exclamation.svg')
  
    turn_up = os.fspath(solid_dir / 'turn-up.svg')
  
    user_slash = os.fspath(solid_dir / 'user-slash.svg')
  
    percent = os.fspath(solid_dir / 'percent.svg')
  
    face_rolling_eyes = os.fspath(solid_dir / 'face-rolling-eyes.svg')
  
    gas_pump = os.fspath(solid_dir / 'gas-pump.svg')
  
    box_tissue = os.fspath(solid_dir / 'box-tissue.svg')
  
    up_long = os.fspath(solid_dir / 'up-long.svg')
  
    money_bill_wave = os.fspath(solid_dir / 'money-bill-wave.svg')
  
    panorama = os.fspath(solid_dir / 'panorama.svg')
  
    terminal = os.fspath(solid_dir / 'terminal.svg')
  
    file = os.fspath(solid_dir / 'file.svg')
  
    braille = os.fspath(solid_dir / 'braille.svg')
  
    igloo = os.fspath(solid_dir / 'igloo.svg')
  
    suitcase_rolling = os.fspath(solid_dir / 'suitcase-rolling.svg')
  
    file_circle_check = os.fspath(solid_dir / 'file-circle-check.svg')
  
    masks_theater = os.fspath(solid_dir / 'masks-theater.svg')
  
    sack_dollar = os.fspath(solid_dir / 'sack-dollar.svg')
  
    caravan = os.fspath(solid_dir / 'caravan.svg')
  
    unlock = os.fspath(solid_dir / 'unlock.svg')
  
    temperature_three_quarters = os.fspath(solid_dir / 'temperature-three-quarters.svg')
  
    chevron_up = os.fspath(solid_dir / 'chevron-up.svg')
  
    fill = os.fspath(solid_dir / 'fill.svg')
  
    road = os.fspath(solid_dir / 'road.svg')
  
    square_pen = os.fspath(solid_dir / 'square-pen.svg')
  
    hand_holding_dollar = os.fspath(solid_dir / 'hand-holding-dollar.svg')
  
    trademark = os.fspath(solid_dir / 'trademark.svg')
  
    fish_fins = os.fspath(solid_dir / 'fish-fins.svg')
  
    satellite_dish = os.fspath(solid_dir / 'satellite-dish.svg')
  
    exclamation = os.fspath(solid_dir / 'exclamation.svg')
  
    puzzle_piece = os.fspath(solid_dir / 'puzzle-piece.svg')
  
    child = os.fspath(solid_dir / 'child.svg')
  
    up_down_left_right = os.fspath(solid_dir / 'up-down-left-right.svg')
  
    list_check = os.fspath(solid_dir / 'list-check.svg')
  
    diamond_turn_right = os.fspath(solid_dir / 'diamond-turn-right.svg')
  
    code = os.fspath(solid_dir / 'code.svg')
  
    scroll = os.fspath(solid_dir / 'scroll.svg')
  
    house_lock = os.fspath(solid_dir / 'house-lock.svg')
  
    sort = os.fspath(solid_dir / 'sort.svg')
  
    arrow_up_from_water_pump = os.fspath(solid_dir / 'arrow-up-from-water-pump.svg')
  
    user_group = os.fspath(solid_dir / 'user-group.svg')
  
    globe = os.fspath(solid_dir / 'globe.svg')
  
    rupee_sign = os.fspath(solid_dir / 'rupee-sign.svg')
  
    e = os.fspath(solid_dir / 'e.svg')
  
    comment_dollar = os.fspath(solid_dir / 'comment-dollar.svg')
  
    users_viewfinder = os.fspath(solid_dir / 'users-viewfinder.svg')
  
    dice = os.fspath(solid_dir / 'dice.svg')
  
    smog = os.fspath(solid_dir / 'smog.svg')
  
    calculator = os.fspath(solid_dir / 'calculator.svg')
  
    won_sign = os.fspath(solid_dir / 'won-sign.svg')
  
    users_between_lines = os.fspath(solid_dir / 'users-between-lines.svg')
  
    toilet_paper = os.fspath(solid_dir / 'toilet-paper.svg')
  
    building_shield = os.fspath(solid_dir / 'building-shield.svg')
  
    flask_vial = os.fspath(solid_dir / 'flask-vial.svg')
  
    circle_info = os.fspath(solid_dir / 'circle-info.svg')
  
    user_plus = os.fspath(solid_dir / 'user-plus.svg')
  
    spell_check = os.fspath(solid_dir / 'spell-check.svg')
  
    closed_captioning = os.fspath(solid_dir / 'closed-captioning.svg')
  
    chess = os.fspath(solid_dir / 'chess.svg')
  
    colon_sign = os.fspath(solid_dir / 'colon-sign.svg')
  
    chart_line = os.fspath(solid_dir / 'chart-line.svg')
  
    cent_sign = os.fspath(solid_dir / 'cent-sign.svg')
  
    person_snowboarding = os.fspath(solid_dir / 'person-snowboarding.svg')
  
    battery_quarter = os.fspath(solid_dir / 'battery-quarter.svg')
  
    f = os.fspath(solid_dir / 'f.svg')
  
    star_of_life = os.fspath(solid_dir / 'star-of-life.svg')
  
    arrows_down_to_line = os.fspath(solid_dir / 'arrows-down-to-line.svg')
  
    p = os.fspath(solid_dir / 'p.svg')
  
    utensils = os.fspath(solid_dir / 'utensils.svg')
  
    lock_open = os.fspath(solid_dir / 'lock-open.svg')
  
    image_portrait = os.fspath(solid_dir / 'image-portrait.svg')
  
    school_lock = os.fspath(solid_dir / 'school-lock.svg')
  
    temperature_full = os.fspath(solid_dir / 'temperature-full.svg')
  
    square_arrow_up_right = os.fspath(solid_dir / 'square-arrow-up-right.svg')
  
    arrow_left = os.fspath(solid_dir / 'arrow-left.svg')
  
    anchor_circle_check = os.fspath(solid_dir / 'anchor-circle-check.svg')
  
    cube = os.fspath(solid_dir / 'cube.svg')
  
    anchor = os.fspath(solid_dir / 'anchor.svg')
  
    hand_back_fist = os.fspath(solid_dir / 'hand-back-fist.svg')
  
    scale_balanced = os.fspath(solid_dir / 'scale-balanced.svg')
  
    user_xmark = os.fspath(solid_dir / 'user-xmark.svg')
  
    crow = os.fspath(solid_dir / 'crow.svg')
  
    forward_fast = os.fspath(solid_dir / 'forward-fast.svg')
  
    truck_fast = os.fspath(solid_dir / 'truck-fast.svg')
  
    bus = os.fspath(solid_dir / 'bus.svg')
  
    user_injured = os.fspath(solid_dir / 'user-injured.svg')
  
    basket_shopping = os.fspath(solid_dir / 'basket-shopping.svg')
  
    staff_snake = os.fspath(solid_dir / 'staff-snake.svg')
  
    mobile = os.fspath(solid_dir / 'mobile.svg')
  
    cart_plus = os.fspath(solid_dir / 'cart-plus.svg')
  
    diagram_successor = os.fspath(solid_dir / 'diagram-successor.svg')
  
    hat_wizard = os.fspath(solid_dir / 'hat-wizard.svg')
  
    square_phone_flip = os.fspath(solid_dir / 'square-phone-flip.svg')
  
    table = os.fspath(solid_dir / 'table.svg')
  
    server = os.fspath(solid_dir / 'server.svg')
  
    trailer = os.fspath(solid_dir / 'trailer.svg')
  
    bag_shopping = os.fspath(solid_dir / 'bag-shopping.svg')
  
    notes_medical = os.fspath(solid_dir / 'notes-medical.svg')
  
    money_bill_trend_up = os.fspath(solid_dir / 'money-bill-trend-up.svg')
  
    cookie = os.fspath(solid_dir / 'cookie.svg')
  
    building_wheat = os.fspath(solid_dir / 'building-wheat.svg')
  
    hand_holding_hand = os.fspath(solid_dir / 'hand-holding-hand.svg')
  
    slash = os.fspath(solid_dir / 'slash.svg')
  
    house_flag = os.fspath(solid_dir / 'house-flag.svg')
  
    child_dress = os.fspath(solid_dir / 'child-dress.svg')
  
    virus_covid = os.fspath(solid_dir / 'virus-covid.svg')
  
    file_export = os.fspath(solid_dir / 'file-export.svg')
  
    arrows_turn_to_dots = os.fspath(solid_dir / 'arrows-turn-to-dots.svg')
  
    trash_arrow_up = os.fspath(solid_dir / 'trash-arrow-up.svg')
  
    layer_group = os.fspath(solid_dir / 'layer-group.svg')
  
    hard_drive = os.fspath(solid_dir / 'hard-drive.svg')
  
    square_caret_down = os.fspath(solid_dir / 'square-caret-down.svg')
  
    film = os.fspath(solid_dir / 'film.svg')
  
    file_circle_question = os.fspath(solid_dir / 'file-circle-question.svg')
  
    plane_arrival = os.fspath(solid_dir / 'plane-arrival.svg')
  
    coins = os.fspath(solid_dir / 'coins.svg')
  
    arrow_pointer = os.fspath(solid_dir / 'arrow-pointer.svg')
  
    snowman = os.fspath(solid_dir / 'snowman.svg')
  
    archway = os.fspath(solid_dir / 'archway.svg')
  
    otter = os.fspath(solid_dir / 'otter.svg')
  
    wind = os.fspath(solid_dir / 'wind.svg')
  
    file_import = os.fspath(solid_dir / 'file-import.svg')
  
    circle_h = os.fspath(solid_dir / 'circle-h.svg')
  
    cross = os.fspath(solid_dir / 'cross.svg')
  
    person_walking_arrow_right = os.fspath(solid_dir / 'person-walking-arrow-right.svg')
  
    face_grin_tears = os.fspath(solid_dir / 'face-grin-tears.svg')
  
    compress = os.fspath(solid_dir / 'compress.svg')
  
    bolt_lightning = os.fspath(solid_dir / 'bolt-lightning.svg')
  
    mortar_pestle = os.fspath(solid_dir / 'mortar-pestle.svg')
  
    sort_up = os.fspath(solid_dir / 'sort-up.svg')
  
    tent_arrows_down = os.fspath(solid_dir / 'tent-arrows-down.svg')
  
    face_grin_beam = os.fspath(solid_dir / 'face-grin-beam.svg')
  
    republican = os.fspath(solid_dir / 'republican.svg')
  
    circle_dollar_to_slot = os.fspath(solid_dir / 'circle-dollar-to-slot.svg')
  
    plug_circle_check = os.fspath(solid_dir / 'plug-circle-check.svg')
  
    solar_panel = os.fspath(solid_dir / 'solar-panel.svg')
  
    cloud_sun_rain = os.fspath(solid_dir / 'cloud-sun-rain.svg')
  
    calendar_day = os.fspath(solid_dir / 'calendar-day.svg')
  
    ghost = os.fspath(solid_dir / 'ghost.svg')
  
    atom = os.fspath(solid_dir / 'atom.svg')
  
    tty = os.fspath(solid_dir / 'tty.svg')
  
    gear = os.fspath(solid_dir / 'gear.svg')
  
    person_falling_burst = os.fspath(solid_dir / 'person-falling-burst.svg')
  
    dove = os.fspath(solid_dir / 'dove.svg')
  
    cloud_arrow_down = os.fspath(solid_dir / 'cloud-arrow-down.svg')
  
    eye = os.fspath(solid_dir / 'eye.svg')
  
    tag = os.fspath(solid_dir / 'tag.svg')
  
    user_check = os.fspath(solid_dir / 'user-check.svg')
  
    object_ungroup = os.fspath(solid_dir / 'object-ungroup.svg')
  
    bath = os.fspath(solid_dir / 'bath.svg')
  
    umbrella = os.fspath(solid_dir / 'umbrella.svg')
  
    building_circle_arrow_right = os.fspath(solid_dir / 'building-circle-arrow-right.svg')
  
    camera_rotate = os.fspath(solid_dir / 'camera-rotate.svg')
  
    _3 = os.fspath(solid_dir / '3.svg')
  
    envelope_open_text = os.fspath(solid_dir / 'envelope-open-text.svg')
  
    arrow_down_up_lock = os.fspath(solid_dir / 'arrow-down-up-lock.svg')
  
    tent_arrow_down_to_line = os.fspath(solid_dir / 'tent-arrow-down-to-line.svg')
  
    locust = os.fspath(solid_dir / 'locust.svg')
  
    scale_unbalanced = os.fspath(solid_dir / 'scale-unbalanced.svg')
  
    plug_circle_xmark = os.fspath(solid_dir / 'plug-circle-xmark.svg')
  
    d = os.fspath(solid_dir / 'd.svg')
  
    arrows_split_up_and_left = os.fspath(solid_dir / 'arrows-split-up-and-left.svg')
  
    car_burst = os.fspath(solid_dir / 'car-burst.svg')
  
    id_card = os.fspath(solid_dir / 'id-card.svg')
  
    arrow_rotate_right = os.fspath(solid_dir / 'arrow-rotate-right.svg')
  
    arrows_to_eye = os.fspath(solid_dir / 'arrows-to-eye.svg')
  
    hamsa = os.fspath(solid_dir / 'hamsa.svg')
  
    arrow_down_long = os.fspath(solid_dir / 'arrow-down-long.svg')
  
    ribbon = os.fspath(solid_dir / 'ribbon.svg')
  
    hand_point_up = os.fspath(solid_dir / 'hand-point-up.svg')
  
    pause = os.fspath(solid_dir / 'pause.svg')
  
    headphones_simple = os.fspath(solid_dir / 'headphones-simple.svg')
  
    rug = os.fspath(solid_dir / 'rug.svg')
  
    battery_full = os.fspath(solid_dir / 'battery-full.svg')
  
    shop = os.fspath(solid_dir / 'shop.svg')
  
    wand_magic_sparkles = os.fspath(solid_dir / 'wand-magic-sparkles.svg')
  
    arrow_up_z_a = os.fspath(solid_dir / 'arrow-up-z-a.svg')
  
    wheelchair_move = os.fspath(solid_dir / 'wheelchair-move.svg')
  
    sliders = os.fspath(solid_dir / 'sliders.svg')
  
    torii_gate = os.fspath(solid_dir / 'torii-gate.svg')
  
    calendar_xmark = os.fspath(solid_dir / 'calendar-xmark.svg')
  
    hands_bubbles = os.fspath(solid_dir / 'hands-bubbles.svg')
  
    right_left = os.fspath(solid_dir / 'right-left.svg')
  
    hippo = os.fspath(solid_dir / 'hippo.svg')
  
    door_closed = os.fspath(solid_dir / 'door-closed.svg')
  
    hospital = os.fspath(solid_dir / 'hospital.svg')
  
    caret_left = os.fspath(solid_dir / 'caret-left.svg')
  
    clock_rotate_left = os.fspath(solid_dir / 'clock-rotate-left.svg')
  
    arrow_up_right_from_square = os.fspath(solid_dir / 'arrow-up-right-from-square.svg')
  
    building_lock = os.fspath(solid_dir / 'building-lock.svg')
  
    square_full = os.fspath(solid_dir / 'square-full.svg')
  
    n = os.fspath(solid_dir / 'n.svg')
  
    pump_medical = os.fspath(solid_dir / 'pump-medical.svg')
  
    clipboard_question = os.fspath(solid_dir / 'clipboard-question.svg')
  
    beer_mug_empty = os.fspath(solid_dir / 'beer-mug-empty.svg')
  
    star = os.fspath(solid_dir / 'star.svg')
  
    toggle_off = os.fspath(solid_dir / 'toggle-off.svg')
  
    children = os.fspath(solid_dir / 'children.svg')
  
    arrow_up_1_9 = os.fspath(solid_dir / 'arrow-up-1-9.svg')
  
    burger = os.fspath(solid_dir / 'burger.svg')
  
    building_circle_check = os.fspath(solid_dir / 'building-circle-check.svg')
  
    plane_departure = os.fspath(solid_dir / 'plane-departure.svg')
  
    signature = os.fspath(solid_dir / 'signature.svg')
  
    bold = os.fspath(solid_dir / 'bold.svg')
  
    martini_glass_citrus = os.fspath(solid_dir / 'martini-glass-citrus.svg')
  
    plug_circle_plus = os.fspath(solid_dir / 'plug-circle-plus.svg')
  
    at = os.fspath(solid_dir / 'at.svg')
  
    circle_arrow_down = os.fspath(solid_dir / 'circle-arrow-down.svg')
  
    volleyball = os.fspath(solid_dir / 'volleyball.svg')
  
    hammer = os.fspath(solid_dir / 'hammer.svg')
  
    arrow_down = os.fspath(solid_dir / 'arrow-down.svg')
  
    arrow_up_from_bracket = os.fspath(solid_dir / 'arrow-up-from-bracket.svg')
  
    angle_up = os.fspath(solid_dir / 'angle-up.svg')
  
    face_grimace = os.fspath(solid_dir / 'face-grimace.svg')
  
    right_long = os.fspath(solid_dir / 'right-long.svg')
  
    magnifying_glass_arrow_right = os.fspath(solid_dir / 'magnifying-glass-arrow-right.svg')
  
    t = os.fspath(solid_dir / 't.svg')
  
    person_walking_with_cane = os.fspath(solid_dir / 'person-walking-with-cane.svg')
  
    crosshairs = os.fspath(solid_dir / 'crosshairs.svg')
  
    worm = os.fspath(solid_dir / 'worm.svg')
  
    pallet = os.fspath(solid_dir / 'pallet.svg')
  
    users_slash = os.fspath(solid_dir / 'users-slash.svg')
  
    angle_right = os.fspath(solid_dir / 'angle-right.svg')
  
    tablet_screen_button = os.fspath(solid_dir / 'tablet-screen-button.svg')
  
    virus_covid_slash = os.fspath(solid_dir / 'virus-covid-slash.svg')
  
    people_arrows = os.fspath(solid_dir / 'people-arrows.svg')
  
    house_signal = os.fspath(solid_dir / 'house-signal.svg')
  
    face_grin_beam_sweat = os.fspath(solid_dir / 'face-grin-beam-sweat.svg')
  
    pen_fancy = os.fspath(solid_dir / 'pen-fancy.svg')
  
    pen_nib = os.fspath(solid_dir / 'pen-nib.svg')
  
    bridge_circle_check = os.fspath(solid_dir / 'bridge-circle-check.svg')
  
    square_caret_up = os.fspath(solid_dir / 'square-caret-up.svg')
  
    ellipsis = os.fspath(solid_dir / 'ellipsis.svg')
  
    circle_half_stroke = os.fspath(solid_dir / 'circle-half-stroke.svg')
  
    face_dizzy = os.fspath(solid_dir / 'face-dizzy.svg')
  
    bars = os.fspath(solid_dir / 'bars.svg')
  
    calendar_minus = os.fspath(solid_dir / 'calendar-minus.svg')
  
    monument = os.fspath(solid_dir / 'monument.svg')
  
    w = os.fspath(solid_dir / 'w.svg')
  
    minus = os.fspath(solid_dir / 'minus.svg')
  
    angles_down = os.fspath(solid_dir / 'angles-down.svg')
  
    square_parking = os.fspath(solid_dir / 'square-parking.svg')
  
    thumbtack = os.fspath(solid_dir / 'thumbtack.svg')
  
    right_from_bracket = os.fspath(solid_dir / 'right-from-bracket.svg')
  
    mosquito_net = os.fspath(solid_dir / 'mosquito-net.svg')
  
    handcuffs = os.fspath(solid_dir / 'handcuffs.svg')
  
    face_grin_tongue_squint = os.fspath(solid_dir / 'face-grin-tongue-squint.svg')
  
    clipboard = os.fspath(solid_dir / 'clipboard.svg')
  
    q = os.fspath(solid_dir / 'q.svg')
  
    face_grin_tongue = os.fspath(solid_dir / 'face-grin-tongue.svg')
  
    truck_arrow_right = os.fspath(solid_dir / 'truck-arrow-right.svg')
  
    person_skating = os.fspath(solid_dir / 'person-skating.svg')
  
    hand_point_left = os.fspath(solid_dir / 'hand-point-left.svg')
  
    shower = os.fspath(solid_dir / 'shower.svg')
  
    broom_ball = os.fspath(solid_dir / 'broom-ball.svg')
  
    stroopwafel = os.fspath(solid_dir / 'stroopwafel.svg')
  
    arrow_up = os.fspath(solid_dir / 'arrow-up.svg')
  
    chart_gantt = os.fspath(solid_dir / 'chart-gantt.svg')
  
    plane_circle_xmark = os.fspath(solid_dir / 'plane-circle-xmark.svg')
  
    shield_heart = os.fspath(solid_dir / 'shield-heart.svg')
  
    desktop = os.fspath(solid_dir / 'desktop.svg')
  
    tags = os.fspath(solid_dir / 'tags.svg')
  
    fax = os.fspath(solid_dir / 'fax.svg')
  
    pills = os.fspath(solid_dir / 'pills.svg')
  
    mattress_pillow = os.fspath(solid_dir / 'mattress-pillow.svg')
  
    shield = os.fspath(solid_dir / 'shield.svg')
  
    face_grin_stars = os.fspath(solid_dir / 'face-grin-stars.svg')
  
    shuttle_space = os.fspath(solid_dir / 'shuttle-space.svg')
  
    helicopter = os.fspath(solid_dir / 'helicopter.svg')
  
    circle_right = os.fspath(solid_dir / 'circle-right.svg')
  
    bridge_circle_exclamation = os.fspath(solid_dir / 'bridge-circle-exclamation.svg')
  
    arrow_up_a_z = os.fspath(solid_dir / 'arrow-up-a-z.svg')
  
    shield_virus = os.fspath(solid_dir / 'shield-virus.svg')
  
    laptop_medical = os.fspath(solid_dir / 'laptop-medical.svg')
  
    certificate = os.fspath(solid_dir / 'certificate.svg')
  
    user_nurse = os.fspath(solid_dir / 'user-nurse.svg')
  
    money_check_dollar = os.fspath(solid_dir / 'money-check-dollar.svg')
  
    magnifying_glass_dollar = os.fspath(solid_dir / 'magnifying-glass-dollar.svg')
  
    cloud_meatball = os.fspath(solid_dir / 'cloud-meatball.svg')
  
    car_side = os.fspath(solid_dir / 'car-side.svg')
  
    arrow_up_short_wide = os.fspath(solid_dir / 'arrow-up-short-wide.svg')
  
    truck_pickup = os.fspath(solid_dir / 'truck-pickup.svg')
  
    martini_glass_empty = os.fspath(solid_dir / 'martini-glass-empty.svg')
  
    file_circle_xmark = os.fspath(solid_dir / 'file-circle-xmark.svg')
  
    egg = os.fspath(solid_dir / 'egg.svg')
  
    thumbs_down = os.fspath(solid_dir / 'thumbs-down.svg')
  
    splotch = os.fspath(solid_dir / 'splotch.svg')
  
    _2 = os.fspath(solid_dir / '2.svg')
  
    phone_slash = os.fspath(solid_dir / 'phone-slash.svg')
  
    code_merge = os.fspath(solid_dir / 'code-merge.svg')
  
    face_grin_wink = os.fspath(solid_dir / 'face-grin-wink.svg')
  
    section = os.fspath(solid_dir / 'section.svg')
  
    square_up_right = os.fspath(solid_dir / 'square-up-right.svg')
  
    thumbs_up = os.fspath(solid_dir / 'thumbs-up.svg')
  
    hand_point_down = os.fspath(solid_dir / 'hand-point-down.svg')
  
    ranking_star = os.fspath(solid_dir / 'ranking-star.svg')
  
    socks = os.fspath(solid_dir / 'socks.svg')
  
    trophy = os.fspath(solid_dir / 'trophy.svg')
  
    crop = os.fspath(solid_dir / 'crop.svg')
  
    arrow_down_up_across_line = os.fspath(solid_dir / 'arrow-down-up-across-line.svg')
  
    soap = os.fspath(solid_dir / 'soap.svg')
  
    backward_step = os.fspath(solid_dir / 'backward-step.svg')
  
    circle_arrow_left = os.fspath(solid_dir / 'circle-arrow-left.svg')
  
    earth_asia = os.fspath(solid_dir / 'earth-asia.svg')
  
    star_half = os.fspath(solid_dir / 'star-half.svg')
  
    magnifying_glass_plus = os.fspath(solid_dir / 'magnifying-glass-plus.svg')
  
    helmet_safety = os.fspath(solid_dir / 'helmet-safety.svg')
  
    mars_double = os.fspath(solid_dir / 'mars-double.svg')
  
    brush = os.fspath(solid_dir / 'brush.svg')
  
    rainbow = os.fspath(solid_dir / 'rainbow.svg')
  
    person_shelter = os.fspath(solid_dir / 'person-shelter.svg')
  
    bolt = os.fspath(solid_dir / 'bolt.svg')
  
    forward = os.fspath(solid_dir / 'forward.svg')
  
    spaghetti_monster_flying = os.fspath(solid_dir / 'spaghetti-monster-flying.svg')
  
    square_virus = os.fspath(solid_dir / 'square-virus.svg')
  
    cart_shopping = os.fspath(solid_dir / 'cart-shopping.svg')
  
    square_envelope = os.fspath(solid_dir / 'square-envelope.svg')
  
    venus = os.fspath(solid_dir / 'venus.svg')
  
    bug_slash = os.fspath(solid_dir / 'bug-slash.svg')
  
    square_root_variable = os.fspath(solid_dir / 'square-root-variable.svg')
  
    cruzeiro_sign = os.fspath(solid_dir / 'cruzeiro-sign.svg')
  
    bucket = os.fspath(solid_dir / 'bucket.svg')
  
    _5 = os.fspath(solid_dir / '5.svg')
  
    viruses = os.fspath(solid_dir / 'viruses.svg')
  
    arrows_down_to_people = os.fspath(solid_dir / 'arrows-down-to-people.svg')
  
    file_invoice_dollar = os.fspath(solid_dir / 'file-invoice-dollar.svg')
  
    austral_sign = os.fspath(solid_dir / 'austral-sign.svg')
  
    palette = os.fspath(solid_dir / 'palette.svg')
  
    church = os.fspath(solid_dir / 'church.svg')
  
    right_to_bracket = os.fspath(solid_dir / 'right-to-bracket.svg')
  
    _9 = os.fspath(solid_dir / '9.svg')
  
    earth_africa = os.fspath(solid_dir / 'earth-africa.svg')
  
    person_running = os.fspath(solid_dir / 'person-running.svg')
  
    cloud_showers_heavy = os.fspath(solid_dir / 'cloud-showers-heavy.svg')
  
    weight_scale = os.fspath(solid_dir / 'weight-scale.svg')
  
    circle_xmark = os.fspath(solid_dir / 'circle-xmark.svg')
  
    i_cursor = os.fspath(solid_dir / 'i-cursor.svg')
  
    _4 = os.fspath(solid_dir / '4.svg')
  
    square_rss = os.fspath(solid_dir / 'square-rss.svg')
  
    bitcoin_sign = os.fspath(solid_dir / 'bitcoin-sign.svg')
  
    people_carry_box = os.fspath(solid_dir / 'people-carry-box.svg')
  
    kitchen_set = os.fspath(solid_dir / 'kitchen-set.svg')
  
    road_lock = os.fspath(solid_dir / 'road-lock.svg')
  
    h = os.fspath(solid_dir / 'h.svg')
  
    person_harassing = os.fspath(solid_dir / 'person-harassing.svg')
  
    wifi = os.fspath(solid_dir / 'wifi.svg')
  
    peso_sign = os.fspath(solid_dir / 'peso-sign.svg')
  
    chess_queen = os.fspath(solid_dir / 'chess-queen.svg')
  
    folder_minus = os.fspath(solid_dir / 'folder-minus.svg')
  
    cloud_moon_rain = os.fspath(solid_dir / 'cloud-moon-rain.svg')
  
    face_grin = os.fspath(solid_dir / 'face-grin.svg')
  
    circle_notch = os.fspath(solid_dir / 'circle-notch.svg')
  
    hand_pointer = os.fspath(solid_dir / 'hand-pointer.svg')
  
    location_dot = os.fspath(solid_dir / 'location-dot.svg')
  
    greater_than = os.fspath(solid_dir / 'greater-than.svg')
  
    tablet_button = os.fspath(solid_dir / 'tablet-button.svg')
  
    temperature_half = os.fspath(solid_dir / 'temperature-half.svg')
  
    hand_spock = os.fspath(solid_dir / 'hand-spock.svg')
  
    bell_concierge = os.fspath(solid_dir / 'bell-concierge.svg')
  
    person_half_dress = os.fspath(solid_dir / 'person-half-dress.svg')
  
    file_invoice = os.fspath(solid_dir / 'file-invoice.svg')
  
    skull = os.fspath(solid_dir / 'skull.svg')
  
    file_powerpoint = os.fspath(solid_dir / 'file-powerpoint.svg')
  
    link_slash = os.fspath(solid_dir / 'link-slash.svg')
  
    bowling_ball = os.fspath(solid_dir / 'bowling-ball.svg')
  
    lock = os.fspath(solid_dir / 'lock.svg')
  
    ice_cream = os.fspath(solid_dir / 'ice-cream.svg')
  
    pump_soap = os.fspath(solid_dir / 'pump-soap.svg')
  
    tower_cell = os.fspath(solid_dir / 'tower-cell.svg')
  
    house_medical_circle_exclamation = os.fspath(solid_dir / 'house-medical-circle-exclamation.svg')
  
    peace = os.fspath(solid_dir / 'peace.svg')
  
    record_vinyl = os.fspath(solid_dir / 'record-vinyl.svg')
  
    person_circle_check = os.fspath(solid_dir / 'person-circle-check.svg')
  
    toilet_paper_slash = os.fspath(solid_dir / 'toilet-paper-slash.svg')
  
    plug = os.fspath(solid_dir / 'plug.svg')
  
    phone_flip = os.fspath(solid_dir / 'phone-flip.svg')
  
    person = os.fspath(solid_dir / 'person.svg')
  
    house_flood_water_circle_arrow_right = os.fspath(solid_dir / 'house-flood-water-circle-arrow-right.svg')
  
    lungs = os.fspath(solid_dir / 'lungs.svg')
  
    table_columns = os.fspath(solid_dir / 'table-columns.svg')
  
    diagram_predecessor = os.fspath(solid_dir / 'diagram-predecessor.svg')
  
    link = os.fspath(solid_dir / 'link.svg')
  
    glass_water = os.fspath(solid_dir / 'glass-water.svg')
  
    chalkboard_user = os.fspath(solid_dir / 'chalkboard-user.svg')
  
    arrows_left_right = os.fspath(solid_dir / 'arrows-left-right.svg')
  
    arrows_rotate = os.fspath(solid_dir / 'arrows-rotate.svg')
  
    tablet = os.fspath(solid_dir / 'tablet.svg')
  
    heading = os.fspath(solid_dir / 'heading.svg')
  
    person_dress_burst = os.fspath(solid_dir / 'person-dress-burst.svg')
  
    arrow_right_from_bracket = os.fspath(solid_dir / 'arrow-right-from-bracket.svg')
  
    computer = os.fspath(solid_dir / 'computer.svg')
  
    bars_progress = os.fspath(solid_dir / 'bars-progress.svg')
  
    paperclip = os.fspath(solid_dir / 'paperclip.svg')
  
    head_side_cough_slash = os.fspath(solid_dir / 'head-side-cough-slash.svg')
  
    qrcode = os.fspath(solid_dir / 'qrcode.svg')
  
    oil_well = os.fspath(solid_dir / 'oil-well.svg')
  
    venus_mars = os.fspath(solid_dir / 'venus-mars.svg')
  
    bore_hole = os.fspath(solid_dir / 'bore-hole.svg')
  
    sitemap = os.fspath(solid_dir / 'sitemap.svg')
  
    person_military_rifle = os.fspath(solid_dir / 'person-military-rifle.svg')
  
    gift = os.fspath(solid_dir / 'gift.svg')
  
    address_book = os.fspath(solid_dir / 'address-book.svg')
  
    child_combatant = os.fspath(solid_dir / 'child-combatant.svg')
  
    truck = os.fspath(solid_dir / 'truck.svg')
  
    rupiah_sign = os.fspath(solid_dir / 'rupiah-sign.svg')
  
    box = os.fspath(solid_dir / 'box.svg')
  
    hand_holding_droplet = os.fspath(solid_dir / 'hand-holding-droplet.svg')
  
    highlighter = os.fspath(solid_dir / 'highlighter.svg')
  
    eject = os.fspath(solid_dir / 'eject.svg')
  
    backward = os.fspath(solid_dir / 'backward.svg')
  
    bacteria = os.fspath(solid_dir / 'bacteria.svg')
  
    car = os.fspath(solid_dir / 'car.svg')
  
    temperature_arrow_down = os.fspath(solid_dir / 'temperature-arrow-down.svg')
  
    train_subway = os.fspath(solid_dir / 'train-subway.svg')
  
    mars_and_venus = os.fspath(solid_dir / 'mars-and-venus.svg')
  
    skull_crossbones = os.fspath(solid_dir / 'skull-crossbones.svg')
  
    bug = os.fspath(solid_dir / 'bug.svg')
  
    list_ol = os.fspath(solid_dir / 'list-ol.svg')
  
    arrow_right_to_bracket = os.fspath(solid_dir / 'arrow-right-to-bracket.svg')
  
    award = os.fspath(solid_dir / 'award.svg')
  
    users_rectangle = os.fspath(solid_dir / 'users-rectangle.svg')
  
    square_poll_horizontal = os.fspath(solid_dir / 'square-poll-horizontal.svg')
  
    circle_dot = os.fspath(solid_dir / 'circle-dot.svg')
  
    teeth_open = os.fspath(solid_dir / 'teeth-open.svg')
  
    head_side_cough = os.fspath(solid_dir / 'head-side-cough.svg')
  
    greater_than_equal = os.fspath(solid_dir / 'greater-than-equal.svg')
  
    chart_area = os.fspath(solid_dir / 'chart-area.svg')
  
    arrow_turn_up = os.fspath(solid_dir / 'arrow-turn-up.svg')
  
    ellipsis_vertical = os.fspath(solid_dir / 'ellipsis-vertical.svg')
  
    head_side_virus = os.fspath(solid_dir / 'head-side-virus.svg')
  
    timeline = os.fspath(solid_dir / 'timeline.svg')
  
    bookmark = os.fspath(solid_dir / 'bookmark.svg')
  
    circle_user = os.fspath(solid_dir / 'circle-user.svg')
  
    file_circle_exclamation = os.fspath(solid_dir / 'file-circle-exclamation.svg')
  
    people_roof = os.fspath(solid_dir / 'people-roof.svg')
  
    house_chimney_window = os.fspath(solid_dir / 'house-chimney-window.svg')
  
    user_large = os.fspath(solid_dir / 'user-large.svg')
  
    sheet_plastic = os.fspath(solid_dir / 'sheet-plastic.svg')
  
    school_circle_check = os.fspath(solid_dir / 'school-circle-check.svg')
  
    toilet_portable = os.fspath(solid_dir / 'toilet-portable.svg')
  
    newspaper = os.fspath(solid_dir / 'newspaper.svg')
  
    circle = os.fspath(solid_dir / 'circle.svg')
  
    building_flag = os.fspath(solid_dir / 'building-flag.svg')
  
    spider = os.fspath(solid_dir / 'spider.svg')
  
    sack_xmark = os.fspath(solid_dir / 'sack-xmark.svg')
  
    shoe_prints = os.fspath(solid_dir / 'shoe-prints.svg')
  
    face_grin_wide = os.fspath(solid_dir / 'face-grin-wide.svg')
  
    basketball = os.fspath(solid_dir / 'basketball.svg')
  
    circle_exclamation = os.fspath(solid_dir / 'circle-exclamation.svg')
  
    martini_glass = os.fspath(solid_dir / 'martini-glass.svg')
  
    lari_sign = os.fspath(solid_dir / 'lari-sign.svg')
  
    road_circle_exclamation = os.fspath(solid_dir / 'road-circle-exclamation.svg')
  
    barcode = os.fspath(solid_dir / 'barcode.svg')
  
    money_bill_1_wave = os.fspath(solid_dir / 'money-bill-1-wave.svg')
  
    snowflake = os.fspath(solid_dir / 'snowflake.svg')
  
    ruler_vertical = os.fspath(solid_dir / 'ruler-vertical.svg')
  
    dice_three = os.fspath(solid_dir / 'dice-three.svg')
  
    umbrella_beach = os.fspath(solid_dir / 'umbrella-beach.svg')
  
    clover = os.fspath(solid_dir / 'clover.svg')
  
    people_line = os.fspath(solid_dir / 'people-line.svg')
  
    cloud_bolt = os.fspath(solid_dir / 'cloud-bolt.svg')
  
    explosion = os.fspath(solid_dir / 'explosion.svg')
  
    democrat = os.fspath(solid_dir / 'democrat.svg')
  
    location_pin_lock = os.fspath(solid_dir / 'location-pin-lock.svg')
  
    poo = os.fspath(solid_dir / 'poo.svg')
  
    pen_clip = os.fspath(solid_dir / 'pen-clip.svg')
  
    vials = os.fspath(solid_dir / 'vials.svg')
  
    cart_flatbed = os.fspath(solid_dir / 'cart-flatbed.svg')
  
    school_circle_exclamation = os.fspath(solid_dir / 'school-circle-exclamation.svg')
  
    gem = os.fspath(solid_dir / 'gem.svg')
  
    shirt = os.fspath(solid_dir / 'shirt.svg')
  
    circle_radiation = os.fspath(solid_dir / 'circle-radiation.svg')
  
    ticket_simple = os.fspath(solid_dir / 'ticket-simple.svg')
  
    rectangle_ad = os.fspath(solid_dir / 'rectangle-ad.svg')
  
    shuffle = os.fspath(solid_dir / 'shuffle.svg')
  
    money_bill_1 = os.fspath(solid_dir / 'money-bill-1.svg')
  
    droplet_slash = os.fspath(solid_dir / 'droplet-slash.svg')
  
    laptop_file = os.fspath(solid_dir / 'laptop-file.svg')
  
    kit_medical = os.fspath(solid_dir / 'kit-medical.svg')
  
    paste = os.fspath(solid_dir / 'paste.svg')
  
    users_line = os.fspath(solid_dir / 'users-line.svg')
  


def _get_svg_object(fp: str):
    color = BLACK
    if str(config.background_color) == 'black':
        color = WHITE
    return SVGMobject(fp, color=color)


class Brand:
    """Brand SVG files defined in font-awesome/svgs/brands"""
    def __init__(self) -> None:
        pass

    def __getattr__(self, name) -> SVGMobject:
        return _get_svg_object(_Brand.__members__[name].value)


class Regular:
    """Regular SVG files defined in font-awesome/svgs/regular"""
    def __init__(self) -> None:
        pass

    def __getattr__(self, name) -> SVGMobject:
        return _get_svg_object(_Regular.__members__[name].value)


class Solid:
    """Solid SVG files defined in font-awesome/svgs/solid"""
    def __init__(self) -> None:
        pass

    def __getattr__(self, name) -> SVGMobject:
        return _get_svg_object(_Solid.__members__[name].value)


brand = Brand()
regular = Regular()
solid = Solid()