FAQ Page
========

.. _faq:

Frequently Asked Questions
--------------------------

Question 1
^^^^^^^^^^

What is Sphinx?

Answer
  Sphinx is a tool that makes it easy to create intelligent and beautiful documentation.

Question 2
^^^^^^^^^^

How do I use Schema.org in Sphinx?

Answer
  You can embed Schema.org markup in your Sphinx documentation using raw HTML blocks.

.. raw:: html

    <div itemscope itemtype="https://schema.org/FAQPage">
        <div itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
            <h2 itemprop="name">What is Sphinx?</h2>
            <div itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
                <div itemprop="text">
                    Sphinx is a tool that makes it easy to create intelligent and beautiful documentation.
                </div>
            </div>
        </div>
        <div itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
            <h2 itemprop="name">How do I use Schema.org in Sphinx?</h2>
            <div itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
                <div itemprop="text">
                    You can embed Schema.org markup in your Sphinx documentation using raw HTML blocks.
                </div>
            </div>
        </div>
    </div>
