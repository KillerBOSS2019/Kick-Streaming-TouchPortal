Ziggy = {
    "url": "https:\/\/kick.com",
    "port": None,
    "defaults": {},
    "routes": {
        "l5-swagger.default.api": {
            "uri": "documentation",
            "methods": ["GET", "HEAD"]
        },
        "l5-swagger.default.docs": {
            "uri": "docs\/{jsonFile?}",
            "methods": ["GET", "HEAD"]
        },
        "l5-swagger.default.asset": {
            "uri": "docs\/asset\/{asset}",
            "methods": ["GET", "HEAD"]
        },
        "l5-swagger.default.oauth2_callback": {
            "uri": "api\/oauth2-callback",
            "methods": ["GET", "HEAD"]
        },
        "cashier.payment": {
            "uri": "stripe\/payment\/{id}",
            "methods": ["GET", "HEAD"]
        },
        "cashier.webhook": {
            "uri": "stripe\/webhook",
            "methods": ["POST"]
        },
        "nova.login": {
            "uri": "nova\/login",
            "methods": ["POST"]
        },
        "nova.logout": {
            "uri": "nova\/logout",
            "methods": ["GET", "HEAD"]
        },
        "nova.password.request": {
            "uri": "nova\/password\/reset",
            "methods": ["GET", "HEAD"]
        },
        "nova.password.email": {
            "uri": "nova\/password\/email",
            "methods": ["POST"]
        },
        "nova.password.reset": {
            "uri": "nova\/password\/reset\/{token}",
            "methods": ["GET", "HEAD"]
        },
        "mobile-api.get-token": {
            "uri": "mobile\/token",
            "methods": ["POST"]
        },
        "login": {
            "uri": "login",
            "methods": ["GET", "HEAD"]
        },
        "logout": {
            "uri": "logout",
            "methods": ["POST"]
        },
        "register": {
            "uri": "register",
            "methods": ["GET", "HEAD"]
        },
        "password.request": {
            "uri": "password\/reset",
            "methods": ["GET", "HEAD"]
        },
        "password.email": {
            "uri": "password\/email",
            "methods": ["POST"]
        },
        "password.reset": {
            "uri": "password\/reset\/{token}",
            "methods": ["GET", "HEAD"]
        },
        "password.update": {
            "uri": "password\/reset",
            "methods": ["POST"]
        },
        "password.confirm": {
            "uri": "password\/confirm",
            "methods": ["GET", "HEAD"]
        },
        "socialite.redirect": {
            "uri": "socialite\/{provider}",
            "methods": ["POST"]
        },
        "user": {
            "uri": "api\/v1\/user",
            "methods": ["GET", "HEAD"]
        },
        "resource_urls": {
            "uri": "api\/v1\/resource-urls",
            "methods": ["GET", "HEAD"]
        },
        "agreed-terms": {
            "uri": "api\/v1\/signup\/agreed-terms",
            "methods": ["POST"]
        },
        "set-username": {
            "uri": "api\/v1\/signup\/username",
            "methods": ["POST"]
        },
        "signupComplete": {
            "uri": "api\/v1\/signup\/complete",
            "methods": ["POST"]
        },
        "verification.resend": {
            "uri": "api\/v1\/signup\/verification\/resend",
            "methods": ["POST"]
        },
        "verification.send.sms": {
            "uri": "api\/v1\/signup\/send\/sms",
            "methods": ["POST"]
        },
        "verification.send.email": {
            "uri": "api\/v1\/signup\/send\/email",
            "methods": ["POST"]
        },
        "verification.verify.code": {
            "uri": "api\/v1\/signup\/verify\/code",
            "methods": ["POST"]
        },
        "verification.verify.email": {
            "uri": "api\/v1\/signup\/verify\/email",
            "methods": ["POST"]
        },
        "verification.verify.username": {
            "uri": "api\/v1\/signup\/verify\/username",
            "methods": ["POST"]
        },
        "verification.verify.phone": {
            "uri": "api\/v1\/signup\/verify\/phone",
            "methods": ["POST"]
        },
        "verification.verify.login-code": {
            "uri": "api\/v1\/signup\/verify\/login-code",
            "methods": ["POST"]
        },
        "kick.token.create": {
            "uri": "kick-token-provider",
            "methods": ["GET", "HEAD"]
        },
        "channel.checkUsername": {
            "uri": "channels\/check-username\/{username}",
            "methods": ["GET", "HEAD"]
        },
        "api.search": {
            "uri": "api\/search",
            "methods": ["GET", "HEAD"]
        },
        "nova.terms": {
            "uri": "nova\/terms",
            "methods": ["GET", "HEAD"]
        },
        "channel.chat": {
            "uri": "api\/v1\/channels\/{channel}\/chat",
            "methods": ["GET", "HEAD"]
        },
        "channels.followed": {
            "uri": "api\/v1\/channels\/followed",
            "methods": ["GET", "HEAD"]
        },
        "channelLink.reorder": {
            "uri": "api\/v1\/channel-links\/reorder",
            "methods": ["POST"]
        },
        "channel.muteUser": {
            "uri": "api\/v1\/channels\/{channel}\/mute-user",
            "methods": ["POST"]
        },
        "channel.followers": {
            "uri": "api\/v1\/channels\/{channel}\/followers",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.addBadge": {
            "uri": "api\/v1\/channels\/{channel}\/add-badge",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.removeBadge": {
            "uri": "api\/v1\/channels\/{channel}\/remove-badge",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.getFollowersForBadge": {
            "uri": "api\/v1\/channels\/{channel}\/get-followers-for-badge\/{badge}",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channels.supportACreator": {
            "uri": "api\/v1\/channels\/{channel}\/support-a-creator",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "liveChannels.search": {
            "uri": "api\/v1\/live-channels\/{channel}\/search",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "subscriptions.index": {
            "uri": "api\/v1\/subscriptions",
            "methods": ["GET", "HEAD"]
        },
        "subscriptions.subscribers": {
            "uri": "api\/v1\/subscriptions\/subscribers",
            "methods": ["GET", "HEAD"]
        },
        "subscriptions.history": {
            "uri": "api\/v1\/subscriptions\/history",
            "methods": ["GET", "HEAD"]
        },
        "subscriptions.connect_account": {
            "uri": "api\/v1\/subscriptions\/connect-account",
            "methods": ["GET", "HEAD"]
        },
        "subscriptions.create_connect_account": {
            "uri": "api\/v1\/subscriptions\/connect-account",
            "methods": ["POST"]
        },
        "subscriptions.plan": {
            "uri": "api\/v1\/subscriptions\/plan",
            "methods": ["GET", "HEAD"]
        },
        "subscriptions.get_default_payment_method": {
            "uri": "api\/v1\/subscriptions\/default-payment-method",
            "methods": ["GET", "HEAD"]
        },
        "subscriptions.get_payment_methods": {
            "uri": "api\/v1\/subscriptions\/payment-methods",
            "methods": ["GET", "HEAD"]
        },
        "subscriptions.create_payment_method": {
            "uri": "api\/v1\/subscriptions\/payment-methods",
            "methods": ["POST"]
        },
        "subscriptions.remove_payment_method": {
            "uri": "api\/v1\/subscriptions\/payment-methods\/{id}",
            "methods": ["DELETE"]
        },
        "subscriptions.stripe_countries": {
            "uri": "api\/v1\/subscriptions\/stripe-countries",
            "methods": ["GET", "HEAD"]
        },
        "subscriptions.create_setup_intent": {
            "uri": "api\/v1\/subscriptions\/setup-intent",
            "methods": ["GET", "HEAD"]
        },
        "subscriptions.resetable": {
            "uri": "api\/v1\/subscriptions\/reset",
            "methods": ["GET", "HEAD"]
        },
        "subscriptions.reset": {
            "uri": "api\/v1\/subscriptions\/reset",
            "methods": ["DELETE"]
        },
        "subscriptions.stripe_subscribe": {
            "uri": "api\/v1\/subscriptions\/channels\/{channel}\/subscribe",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "subscriptions.get_payments_history": {
            "uri": "api\/v1\/subscriptions\/payments-history",
            "methods": ["GET", "HEAD"]
        },
        "subscriptions.update_payment_method": {
            "uri": "api\/v1\/subscriptions\/{subscription}\/update-payment-method",
            "methods": ["PUT"],
            "bindings": {
                "subscription": "id"
            }
        },
        "subscriptions.cancel": {
            "uri": "api\/v1\/subscriptions\/{subscription}",
            "methods": ["DELETE"],
            "bindings": {
                "subscription": "id"
            }
        },
        "subscriptions.gift-subscriptions": {
            "uri": "api\/v1\/subscriptions\/channels\/{channel}\/gift-subscriptions",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "subscriptions.confirm-payment-intent": {
            "uri": "api\/v1\/subscriptions\/channels\/{channel}\/confirm-payment-intent",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.subscribe": {
            "uri": "api\/v1\/channels\/user\/subscribe",
            "methods": ["POST"]
        },
        "channel.unsubscribe": {
            "uri": "api\/v1\/channels\/user\/unsubscribe",
            "methods": ["POST"]
        },
        "channel.getLivestream": {
            "uri": "api\/v1\/channels\/{channel}\/livestream",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "liveStream.heartBeat": {
            "uri": "api\/v1\/live-streams\/{liveStream}\/heart-beat",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "liveStream": "slug"
            }
        },
        "channel.send": {
            "uri": "api\/v1\/channels\/{channel}\/chat",
            "methods": ["POST"]
        },
        "contentmoderation.reportcontent": {
            "uri": "api\/v1\/report-content",
            "methods": ["POST"]
        },
        "channel.followingSortBy": {
            "uri": "api\/v1\/channels\/following\/{id}",
            "methods": ["GET", "HEAD"]
        },
        "chatroom.show": {
            "uri": "api\/v1\/{channel}\/chatroom",
            "methods": ["GET", "HEAD"]
        },
        "chatroom.update": {
            "uri": "api\/v1\/chatrooms\/{chatroom}",
            "methods": ["PUT"],
            "bindings": {
                "chatroom": "id"
            }
        },
        "chatmessages.store": {
            "uri": "api\/v1\/chat-messages",
            "methods": ["POST"]
        },
        "chatmessages.destroy": {
            "uri": "api\/v1\/chat-messages\/{id}",
            "methods": ["POST"]
        },
        "channel-links.store": {
            "uri": "api\/v1\/channel-links",
            "methods": ["POST"]
        },
        "channel-links.update": {
            "uri": "api\/v1\/channel-links\/{channel_link}",
            "methods": ["PUT", "PATCH"]
        },
        "channel-links.destroy": {
            "uri": "api\/v1\/channel-links\/{channel_link}",
            "methods": ["DELETE"]
        },
        "channels.show": {
            "uri": "api\/v1\/channels\/{channel}",
            "methods": ["GET", "HEAD"]
        },
        "channels.links": {
            "uri": "api\/v1\/channels\/{channel}\/links",
            "methods": ["GET", "HEAD"]
        },
        "user.show": {
            "uri": "api\/v1\/users\/{username}",
            "methods": ["GET", "HEAD"]
        },
        "categories.get": {
            "uri": "api\/v1\/categories",
            "methods": ["GET", "HEAD"]
        },
        "categories.top": {
            "uri": "api\/v1\/categories\/top",
            "methods": ["GET", "HEAD"]
        },
        "user.categories.top": {
            "uri": "api\/v1\/user\/categories\/top",
            "methods": ["GET", "HEAD"]
        },
        "categories.show": {
            "uri": "api\/v1\/categories\/{category}",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "category": "slug"
            }
        },
        "user.livestreams": {
            "uri": "api\/v1\/user\/livestreams",
            "methods": ["GET", "HEAD"]
        },
        "subcategories.get": {
            "uri": "api\/v1\/subcategories",
            "methods": ["GET", "HEAD"]
        },
        "subcategories.all": {
            "uri": "api\/v1\/listsubcategories",
            "methods": ["GET", "HEAD"]
        },
        "subcategories.show": {
            "uri": "api\/v1\/subcategories\/{subcategory}",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "subcategory": "slug"
            }
        },
        "video.show": {
            "uri": "api\/v1\/video\/{video}",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "video": "uuid"
            }
        },
        "video.view": {
            "uri": "api\/v1\/video\/views\/{video}",
            "methods": ["POST"],
            "bindings": {
                "video": "uuid"
            }
        },
        "video.delete": {
            "uri": "api\/v1\/video\/{video}",
            "methods": ["DELETE"],
            "bindings": {
                "video": "uuid"
            }
        },
        "subcategories.toggleFollow": {
            "uri": "api\/v1\/subcategories\/{subcategory}\/toggle-follow",
            "methods": ["POST"],
            "bindings": {
                "subcategory": "slug"
            }
        },
        "banned-users": {
            "uri": "api\/v1\/channels\/{channel}\/banned-users",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "payment.initiateSubscriptionForMobile": {
            "uri": "api\/mobile\/channels\/{channel}\/subscriptions",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "payment.initiateGiftForMobile": {
            "uri": "api\/mobile\/channels\/{channel}\/gift",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "v2.channels.followed": {
            "uri": "api\/v2\/channels\/followed",
            "methods": ["GET", "HEAD"]
        },
        "payment.initiateSubscription": {
            "uri": "api\/v2\/channels\/{channel}\/subscriptions",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "payment.cancelSubscription": {
            "uri": "api\/v2\/channels\/{channel}\/subscriptions",
            "methods": ["DELETE"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.enableSubscription": {
            "uri": "api\/v2\/channels\/{channel}\/subscriptions\/enable",
            "methods": ["PUT"],
            "bindings": {
                "channel": "slug"
            }
        },
        "user.updateFilteredCategories": {
            "uri": "api\/v2\/user\/filtered-categories",
            "methods": ["PUT"]
        },
        "user.getFilteredCategories": {
            "uri": "api\/v2\/user\/filtered-categories",
            "methods": ["GET", "HEAD"]
        },
        "payment.initiateGift": {
            "uri": "api\/v2\/channels\/{channel}\/gift",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.shouldMigrate": {
            "uri": "api\/v2\/channels\/{channel}\/should-migrate",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.migrate": {
            "uri": "api\/v2\/channels\/{channel}\/migrate",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.report": {
            "uri": "api\/v2\/channels\/{channel}\/report",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "poll.create": {
            "uri": "api\/v2\/channels\/{channel}\/polls",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "poll.delete": {
            "uri": "api\/v2\/channels\/{channel}\/polls",
            "methods": ["DELETE"],
            "bindings": {
                "channel": "slug"
            }
        },
        "poll.vote": {
            "uri": "api\/v2\/channels\/{channel}\/polls\/vote",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "pinnedMessage.create": {
            "uri": "api\/v2\/channels\/{channel}\/pinned-message",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "pinnedMessage.delete": {
            "uri": "api\/v2\/channels\/{channel}\/pinned-message",
            "methods": ["DELETE"],
            "bindings": {
                "channel": "slug"
            }
        },
        "payment.listPlans": {
            "uri": "api\/v2\/channels\/{channel}\/plans",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.me": {
            "uri": "api\/v2\/channels\/{channel}\/me",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.follow": {
            "uri": "api\/v2\/channels\/{channel}\/follow",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.unfollow": {
            "uri": "api\/v2\/channels\/{channel}\/follow",
            "methods": ["DELETE"],
            "bindings": {
                "channel": "slug"
            }
        },
        "user.getPaymentProfile": {
            "uri": "api\/v2\/user\/payment-profile",
            "methods": ["GET", "HEAD"]
        },
        "user.addPaymentMethod": {
            "uri": "api\/v2\/user\/payment-methods",
            "methods": ["POST"]
        },
        "user.deletePaymentMethod": {
            "uri": "api\/v2\/user\/payment-methods\/delete",
            "methods": ["POST"]
        },
        "user.changeDefaultPaymentMethod": {
            "uri": "api\/v2\/user\/payment-methods\/default",
            "methods": ["POST"]
        },
        "user.getSubscriptions": {
            "uri": "api\/v2\/user\/subscriptions",
            "methods": ["GET", "HEAD"]
        },
        "chatcommands.send": {
            "uri": "api\/v2\/channels\/{channel}\/chat-commands",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "clip.init": {
            "uri": "api\/v2\/channels\/{channel}\/clips\/init",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "clip.finalize": {
            "uri": "api\/v2\/channels\/{channel}\/clips\/finalize",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "clip.delete": {
            "uri": "api\/v2\/clips\/{clip}",
            "methods": ["DELETE"],
            "bindings": {
                "clip": "id"
            }
        },
        "clip.like": {
            "uri": "api\/v2\/clips\/{clip}\/like",
            "methods": ["PUT"],
            "bindings": {
                "clip": "id"
            }
        },
        "clip.unlike": {
            "uri": "api\/v2\/clips\/{clip}\/like",
            "methods": ["DELETE"],
            "bindings": {
                "clip": "id"
            }
        },
        "ban.list": {
            "uri": "api\/v2\/channels\/{channel}\/bans",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "ban.create": {
            "uri": "api\/v2\/channels\/{channel}\/bans",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "ban.delete": {
            "uri": "api\/v2\/channels\/{channel}\/bans\/{username}",
            "methods": ["DELETE"],
            "bindings": {
                "channel": "slug"
            }
        },
        "subscriber.last": {
            "uri": "api\/v2\/channels\/{channel}\/subscribers\/last",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "user.updateChannelNotifications": {
            "uri": "api\/v2\/user\/channels\/{channel}\/notifications",
            "methods": ["PUT"],
            "bindings": {
                "channel": "slug"
            }
        },
        "mobile-tokens.store": {
            "uri": "api\/v2\/mobile-tokens",
            "methods": ["POST"]
        },
        "mobile-tokens.destroy": {
            "uri": "api\/v2\/mobile-tokens\/{token}",
            "methods": ["DELETE"]
        },
        "chat-identity.update": {
            "uri": "api\/v2\/channels\/{channelId}\/users\/{userId}\/identity",
            "methods": ["PUT"]
        },
        "v2.channels.feed-activities": {
            "uri": "api\/v2\/channels\/feed-activities",
            "methods": ["GET", "HEAD"]
        },
        "chat-history.channeluser-messages": {
            "uri": "api\/v2\/channels\/{channelId}\/users\/{userId}\/messages",
            "methods": ["GET", "HEAD"]
        },
        "security.user.updatePhone": {
            "uri": "api\/v2\/security\/user\/update-phone",
            "methods": ["POST"]
        },
        "livestream.update": {
            "uri": "api\/v2\/stream\/update",
            "methods": ["POST"]
        },
        "user.getVerifiedStatus": {
            "uri": "api\/v2\/user\/verified-status",
            "methods": ["GET", "HEAD"]
        },
        "channel.videos": {
            "uri": "api\/v2\/channels\/{channel}\/videos",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "poll.get": {
            "uri": "api\/v2\/channels\/{channel}\/polls",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "chat-identity.get": {
            "uri": "api\/v2\/channels\/{channelId}\/users\/{userId}\/identity",
            "methods": ["GET", "HEAD"]
        },
        "chat-history.user-messages": {
            "uri": "api\/v2\/users\/{userId}\/messages",
            "methods": ["GET", "HEAD"]
        },
        "chat-history.channel-messages": {
            "uri": "api\/v2\/channels\/{channelId}\/messages",
            "methods": ["GET", "HEAD"]
        },
        "channels.showclean": {
            "uri": "api\/v2\/channels\/{channel}",
            "methods": ["GET", "HEAD"]
        },
        "chat.getUserDetails": {
            "uri": "api\/v2\/channels\/{channel}\/users\/{username}",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.chatroom": {
            "uri": "api\/v2\/channels\/{channel}\/chatroom",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.chatroomModify": {
            "uri": "api\/v2\/channels\/{channel}\/chatroom",
            "methods": ["PUT"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.livestream": {
            "uri": "api\/v2\/channels\/{channel}\/livestream",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "vod.latest": {
            "uri": "api\/v2\/channels\/{channel}\/videos\/latest",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "chatroom.getRules": {
            "uri": "api\/v2\/channels\/{channel}\/chatroom\/rules",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "chatroom.modifyRules": {
            "uri": "api\/v2\/channels\/{channel}\/chatroom\/rules",
            "methods": ["PUT"],
            "bindings": {
                "channel": "slug"
            }
        },
        "chatroom.getBannedwords": {
            "uri": "api\/v2\/channels\/{channel}\/chatroom\/banned-words",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "chatroom.modifyBannedwords": {
            "uri": "api\/v2\/channels\/{channel}\/chatroom\/banned-words",
            "methods": ["PUT"],
            "bindings": {
                "channel": "slug"
            }
        },
        "clip.get": {
            "uri": "api\/v2\/clips\/{clip}",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "clip": "id"
            }
        },
        "clip.listForChannel": {
            "uri": "api\/v2\/channels\/{channel}\/clips",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "clip.setPrivateStatus": {
            "uri": "api\/v2\/clips\/{clip}\/private",
            "methods": ["PUT"],
            "bindings": {
                "clip": "id"
            }
        },
        "clip.getInfo": {
            "uri": "api\/v2\/clips\/{clip}\/info",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "clip": "id"
            }
        },
        "clip.list": {
            "uri": "api\/v2\/clips",
            "methods": ["GET", "HEAD"]
        },
        "clip.listForCategory": {
            "uri": "api\/v2\/categories\/{subcategory}\/clips",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "subcategory": "slug"
            }
        },
        "channel.leaderboards": {
            "uri": "api\/v2\/channels\/{channel}\/leaderboards",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "liveStream.setMature": {
            "uri": "api\/v2\/livestreams\/{liveStream}\/mature",
            "methods": ["PUT"],
            "bindings": {
                "liveStream": "slug"
            }
        },
        "send.chatmessage": {
            "uri": "api\/v2\/messages\/send\/{chatroomId}",
            "methods": ["POST"]
        },
        "delete.chatmessage": {
            "uri": "api\/v2\/chatrooms\/{chatroomId}\/messages\/{messageId}",
            "methods": ["DELETE"]
        },
        "stream.update": {
            "uri": "stream\/update",
            "methods": ["POST"]
        },
        "stream.updateStream": {
            "uri": "stream\/{liveStream}\/update",
            "methods": ["POST"],
            "bindings": {
                "liveStream": "slug"
            }
        },
        "stream.getInfo": {
            "uri": "stream\/info",
            "methods": ["GET", "HEAD"]
        },
        "stream.setInfo": {
            "uri": "stream\/info",
            "methods": ["PUT"]
        },
        "stream.get_publish_token": {
            "uri": "stream\/publish_token",
            "methods": ["GET", "HEAD"]
        },
        "channel.update": {
            "uri": "channels",
            "methods": ["PUT"]
        },
        "channel.addUser": {
            "uri": "channels\/add-user",
            "methods": ["POST"]
        },
        "channel.removeUser": {
            "uri": "channels\/remove-user",
            "methods": ["POST"]
        },
        "emotes.updatePrefix": {
            "uri": "emotes\/prefix",
            "methods": ["PUT"]
        },
        "emotes.index": {
            "uri": "emotes",
            "methods": ["GET", "HEAD"]
        },
        "emotes.store": {
            "uri": "emotes",
            "methods": ["POST"]
        },
        "emotes.destroy": {
            "uri": "emotes\/{emote}",
            "methods": ["DELETE"],
            "bindings": {
                "emote": "id"
            }
        },
        "channel-subscriber-badges.index": {
            "uri": "channel-subscriber-badges",
            "methods": ["GET", "HEAD"]
        },
        "channel-subscriber-badges.store": {
            "uri": "channel-subscriber-badges",
            "methods": ["POST"]
        },
        "channel-subscriber-badges.update": {
            "uri": "channel-subscriber-badges\/{channel_subscriber_badge}",
            "methods": ["PUT", "PATCH"],
            "bindings": {
                "channel_subscriber_badge": "id"
            }
        },
        "channel-subscriber-badges.destroy": {
            "uri": "channel-subscriber-badges\/{channel_subscriber_badge}",
            "methods": ["DELETE"],
            "bindings": {
                "channel_subscriber_badge": "id"
            }
        },
        "user.setup2fa": {
            "uri": "setup-2fa",
            "methods": ["GET", "HEAD"]
        },
        "user.verify2Fa": {
            "uri": "verify-2fa",
            "methods": ["POST"]
        },
        "user.remove2Fa": {
            "uri": "remove-2fa",
            "methods": ["PUT"]
        },
        "stream.languages": {
            "uri": "stream\/languages",
            "methods": ["GET", "HEAD"]
        },
        "profile.default-pictures": {
            "uri": "profile\/default-pictures",
            "methods": ["GET", "HEAD"]
        },
        "profile.update-default-picture": {
            "uri": "profile\/update-default-profile-picture",
            "methods": ["PATCH"]
        },
        "profile.update-default-banner": {
            "uri": "profile\/update-default-banner-picture",
            "methods": ["PATCH"]
        },
        "emotes.channelEmotes": {
            "uri": "emotes\/{channel}",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "stream.livestreams": {
            "uri": "stream\/livestreams\/{lang}",
            "methods": ["GET", "HEAD"]
        },
        "stream.featured.livestreams": {
            "uri": "stream\/featured-livestreams\/{lang}",
            "methods": ["GET", "HEAD"]
        },
        "livestream.viewers": {
            "uri": "current-viewers",
            "methods": ["GET", "HEAD"]
        },
        "featured.livestreams.sidebar": {
            "uri": "featured-livestreams\/non-following",
            "methods": ["GET", "HEAD"]
        },
        "profile.update_profile": {
            "uri": "update_profile",
            "methods": ["POST"]
        },
        "profile.update_password": {
            "uri": "update_password",
            "methods": ["POST"]
        },
        "profile.update-profile-picture": {
            "uri": "profile\/update-profile-picture",
            "methods": ["POST"]
        },
        "profile.update-profile-banner": {
            "uri": "profile\/update-profile-banner",
            "methods": ["POST"]
        },
        "profile.update-notification": {
            "uri": "profile\/update-notifications",
            "methods": ["PATCH"]
        },
        "profile.update-username": {
            "uri": "profile\/update-username",
            "methods": ["PATCH"]
        },
        "profile.update-offline-banner": {
            "uri": "profile\/update-offline-banner-picture",
            "methods": ["PATCH"]
        },
        "chat.username": {
            "uri": "channels\/{channel}\/{username}",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.chatroom.settings.update": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/settings",
            "methods": ["PUT"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.chatroom.bannedwords.get": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/banned-words",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.chatroom.bannedwords.add": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/banned-words",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.chatroom.bannedwords.update": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/banned-words\/{bannedword}",
            "methods": ["PUT"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.chatroom.bannedwords.delete": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/banned-words\/{bannedword}",
            "methods": ["DELETE"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.chatroom.rules.update": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/rules",
            "methods": ["PUT"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channels.live.search": {
            "uri": "api\/internal\/v1\/live\/search",
            "methods": ["GET", "HEAD"]
        },
        "channel.chatroom.identity.update": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/identity",
            "methods": ["PUT"]
        },
        "global.chatroom.identity.update": {
            "uri": "api\/internal\/v1\/chatroom\/identity",
            "methods": ["PUT"]
        },
        "channel.chatroom.pinnedmessage.add": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/pinned-message",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.chatroom.pinnedmessage.remove": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/pinned-message",
            "methods": ["DELETE"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.chatroom.poll.add": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/poll",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.chatroom.poll.remove": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/poll",
            "methods": ["DELETE"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.chatroom.poll.vote": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/poll\/vote",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.community.moderators.get": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/community\/moderators",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.community.moderators.add": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/community\/moderators",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.community.moderators.remove": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/community\/moderators\/{moderator}",
            "methods": ["DELETE"],
            "bindings": {
                "channel": "slug"
            }
        },
        "user.moderators.get": {
            "uri": "api\/internal\/v1\/user\/moderators",
            "methods": ["GET", "HEAD"]
        },
        "channel.community.ogs.get": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/community\/ogs",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.community.ogs.add": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/community\/ogs",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.community.ogs.remove": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/community\/ogs\/{og}",
            "methods": ["DELETE"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.community.vips.get": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/community\/vips",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.community.vips.add": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/community\/vips",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.community.vips.remove": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/community\/vips\/{vip}",
            "methods": ["DELETE"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.events.get": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/events",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.livestreams.events.get": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/events\/livestreams",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "chatroom.events.get": {
            "uri": "api\/internal\/v1\/chatrooms\/{chatroom}\/events",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "chatroom": "id"
            }
        },
        "livestream.events.get": {
            "uri": "api\/internal\/v1\/livestreams\/{livestream}\/events",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "livestream": "slug"
            }
        },
        "channel.chatroom.get": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.followers.count.get": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/followers-count",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.chatroom.settings.get": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/settings",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.chatroom.identity.get": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/users\/{userId}\/identity",
            "methods": ["GET", "HEAD"]
        },
        "global.chatroom.identity.get": {
            "uri": "api\/internal\/v1\/chatroom\/users\/{userId}\/identity",
            "methods": ["GET", "HEAD"]
        },
        "channel.chatroom.rules.get": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/rules",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.chatroom.pinnedmessage.get": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/pinned-message",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.payment.profile.get": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/payment\/profile",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.payment.apple.add": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/payment\/apple",
            "methods": ["POST"],
            "bindings": {
                "channel": "slug"
            }
        },
        "channel.chatroom.poll.get": {
            "uri": "api\/internal\/v1\/channels\/{channel}\/chatroom\/poll",
            "methods": ["GET", "HEAD"],
            "bindings": {
                "channel": "slug"
            }
        },
        "webhooks.sns": {
            "uri": "webhooks\/sns",
            "methods": ["POST"]
        },
        "socialite.appleCallback": {
            "uri": "redirect\/{provider}",
            "methods": ["POST"]
        },
        "home.sitemap": {
            "uri": "sitemap",
            "methods": ["GET", "HEAD"]
        },
        "home.page.legal": {
            "uri": "legal\/{page}",
            "methods": ["GET", "HEAD"]
        },
        "verification.verify": {
            "uri": "email\/verify\/{id}\/{hash}",
            "methods": ["GET", "HEAD"]
        },
        "stripe.payment-intent-redirect": {
            "uri": "payment-intent-redirect",
            "methods": ["GET", "HEAD"]
        },
        "verification.verify-new": {
            "uri": "verify-new-email\/{token}",
            "methods": ["GET", "HEAD"]
        },
        "swagger.getDocs": {
            "uri": "documentation\/api-docs.json",
            "methods": ["GET", "HEAD"]
        },
        "nova.impersonate.take": {
            "uri": "nova-impersonate\/users\/{id}\/{guardName?}",
            "methods": ["GET", "HEAD"]
        },
        "nova.impersonate.leave": {
            "uri": "nova-impersonate\/leave",
            "methods": ["GET", "HEAD"]
        },
        "laravel-nova-excel.download": {
            "uri": "nova-vendor\/maatwebsite\/laravel-nova-excel\/download",
            "methods": ["GET", "HEAD"]
        },
        "app": {
            "uri": "{fallbackPlaceholder}",
            "methods": ["GET", "HEAD"],
            "wheres": {
                "fallbackPlaceholder": ".*"
            }
        }
    }
}
